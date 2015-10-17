var configAuth = require('./auth.js');
var FacebookStrategy = require('passport-facebook').Strategy;
var GoogleStrategy = require('passport-google-oauth').OAuthStrategy;
var User       = require('../app/models/user');
var request = require('request');
var appConfig =require('../config/application');


module.exports = function(passport) {

	passport.serializeUser(function(user, done) {
        done(null, user.id);
    });

    // used to deserialize the user
    passport.deserializeUser(function(id, done) {
        User.findById(id, function(err, user) {
            done(err, user);
        });
    });

	passport.use(new FacebookStrategy({
        clientID        : configAuth.facebookAuth.clientID,
        clientSecret    : configAuth.facebookAuth.clientSecret,
        callbackURL     : configAuth.facebookAuth.callbackURL,
        profileFields	: ['id', 'displayName', 'gender','picture.type(large)', 'email', 'birthday', 'about']
    },

    function(token, refreshToken, profile, done) {
        process.nextTick(function() {
            var newUser            = new User();
            // set all of the facebook information in our user model
            data = profile._json
            newUser.facebook.token = token; // we will save the token that facebook provides to the user
            newUser.facebook.id    = data.id; // set the users facebook id
            newUser.facebook.gender= data.gender
            newUser.facebook.name  = data.name; // look at the passport user profile to see how names are returned
            if(data.email)
                newUser.facebook.email = data.email; // facebook can return multiple emails so we'll take the first
            if(data.picture)
                newUser.facebook.profile_pic_url = data.picture.data.url;
            if(data.birthday)
                newUser.facebook.birthday = data.birthday

            // save our user to the database
            request.post(appConfig.api_base_url+'push_user_profile').form(newUser.toJSON().facebook);
            return done(null, newUser);
        });

    }));

	passport.use(new GoogleStrategy({
	    consumerKey: configAuth.googleAuth.clientID,
	    consumerSecret: configAuth.googleAuth.clientSecret,
	    callbackURL:  configAuth.googleAuth.callbackURL
	 },
	function(token, refreshToken, profile, done) {
        process.nextTick(function() {
        });

    }));
};
