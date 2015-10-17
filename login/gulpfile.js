var fs              = require("fs");
var watchLess = require('gulp-watch-less');
var gulp = require('gulp');
var path            = require("path");
var nodemon         = require('gulp-nodemon')
var less = require('gulp-less');
var nodeInspector   = require('gulp-node-inspector');


gulp.task("less-watch", function(){
	return gulp.src("./assets/css/style.less")
        .pipe(watchLess('./assets/css/style.less'))
        .pipe(less())
        .pipe(gulp.dest('./public/stylesheets/'));
});

gulp.task('inspector', function() {
	console.log('[info] Visit http://devendravm.housing.com:8080/debug?port=5858 to start debugging.')
	return gulp.src([])
	.pipe(nodeInspector({
		preload: false,
	}));
});


gulp.task('server', function () {
	nodemon({
		script: './bin/www',
		watch: ['app', 'config', 'routes'],
		nodeArgs: ['--debug']
	}).on('restart', function () {
	})
});

gulp.task('watch', function () {
	gulp.watch('./assets/**/*.less', ['less-watch'])
});


gulp.task('default', ['watch', 'server', 'inspector']);
