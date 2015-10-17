var path  = require('path');
var fs    =  require('fs')
var less  = require('less');
var through2 = require('through2');
var gutil = require('gulp-util');
var PluginError = gutil.PluginError;
var assign = require('object-assign');
var convert = require('convert-source-map');
var applySourceMap = require('vinyl-sourcemaps-apply');
var assets = require('../server/helpers/assets');
assets.init();

try{
  // TODO: fix this
  var config  = require("../server/config")
} catch (e){
  console.log("Didn't found context.js, waiting for gulp:coffee task", e)
}
var base64Encode = function(filePath){
  try{
    var file = fs.readFileSync(filePath).toString();
    var data = new Buffer(file).toString('base64')
    return "data:image/"+filePath.substr(filePath.lastIndexOf(".")+1, filePath.length)+";base64,"+data;
  } catch(e){
    console.log("[error] Asset Data Path not found for", filePath, e)
    return filePath;
  }
}
module.exports = function (options) {
  // Mixes in default options.
  options = assign({}, {
    compress: false,
    paths: []
  }, options);

  return through2.obj(function(file, enc, cb) {
    if (file.isNull()) {
      return cb(null, file);
    }

    if (file.isStream()) {
      return cb(new PluginError('gulp-less', 'Streaming not supported'));
    }

    var str = file.contents.toString();
    // Clones the options object.
    var opts = assign({}, options);

    // Injects the path of the current file.
    opts.filename = file.path;

    // Bootstrap source maps.
    if (file.sourceMap) {
      opts.sourceMap = {
        sourceMapFileInline: true
      };
    }
    less.render(str, opts)
      .then(function(result, opts){
          result.css = result.css
                      .replace(/(?:image\-url)(?:\()(?:[\'|\"]*)([\S]+)(?:[\'|\"]*)(?:\))/igm,
                              function(a,b,c,d){
                                var _asset = assets.asset_path(b.replace(/[\'\"]/g, ""));
                               if (_asset){
                                //console.log("Replaced", _asset)
                                return "url("+_asset+")"
                               } else {
                                return "url("+_dir.IMAGE_URL+b+")"
                               }
                              })
                      .replace(/(?:font\-url\()(\S+)(\))|(?:font\-url\()(\S+)(\))/igm, function(a,b,c,d,e){
                        if (b || e){
                          b = b?b:e;
                          b = b.replace(/([\'|\"])/ig, "")
                          var index, asset;
                          if ((index = b.indexOf("?#")) != -1){
                            b = b.substr(0, index)
                            asset = assets.asset_path(b)
                            asset += "?#iefix"
                          } else {
                            asset = assets.asset_path(b)
                          }
                          return "url('"+_dir.FONT_PATH+asset+"')";
                        }
                      })
                      .replace(/(?:asset\-data\-url\()(\S+)(\)(\;))|(?:asset\-data\-url\()(\S+)(\))/igm, function(a,b,c,d,e){
                        if (b || e){
                          b = b?b:e;
                          b = b.replace(/([\'|\"])/ig, "")
                          return "url("+base64Encode(_dir.IMAGE_ASSET+b)+")";
                        }
                      });
          file.contents = new Buffer(result.css);
          file.path = gutil.replaceExtension(file.path, '.css');
          console.log("[less-compile] :", file.path)
          if (file.sourceMap) {
            var comment = convert.fromSource(result.css);
            if (comment) {
              file.contents = new Buffer(convert.removeComments(result.css));
              comment.sourcemap.sources = comment.sourcemap.sources.map(function(src){
                return path.relative(file.base, src);
              });
              comment.sourcemap.file = file.relative;
              applySourceMap(file, comment.sourcemap);
            }
          }

          cb(null, file);
    }, function(err){
        // Convert the keys so PluginError can read them
        err.lineNumber = err.line;
        err.fileName = err.filename;

        // Add a better error message
        err.message = err.message + ' in file ' + err.fileName + ' line no. ' + err.lineNumber;

        cb(new PluginError('gulp-less', err), null);
      });
  });
};