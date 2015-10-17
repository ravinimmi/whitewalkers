var sockets= require('../sockets');
// app/routes.js
module.exports = function(app, passport) {

	// =====================================
	// HOME PAGE (with login links) ========
	// =====================================

	app.get('/account', ensureAuthenticated, function(req, res){
	  res.render('account', { user: req.user });
	});

	app.get('/test', function(req, res){
		// user = req.user.toJSON()
		sockets.pushToSockets({message:'news', payload:'test'});
		response.send('Hello World');
		// if(user.facebook)
		// 	profile = user.facebook
		// 	res.render('account', { user: profile });
	});

	app.get('/login', function(req, res){
	  res.render('login', { user: req.user });
	});

	// GET /auth/facebook
	//   Use passport.authenticate() as route middleware to authenticate the
	//   request.  The first step in Facebook authentication will involve
	//   redirecting the user to facebook.com.  After authorization, Facebook will
	//   redirect the user back to this application at /auth/facebook/callback
	app.get('/auth/facebook',
	  passport.authenticate('facebook', { scope : ['public_profile', 'user_birthday', 'email'] }));

	// GET /auth/facebook/callback
	//   Use passport.authenticate() as route middleware to authenticate the
	//   request.  If authentication fails, the user will be redirected back to the
	//   login page.  Otherwise, the primary route function function will be called,
	//   which, in this example, will redirect the user to the home page.
	app.get('/auth/facebook/callback',
	  	passport.authenticate('facebook', {
			failureRedirect : '/'
		}),
	  	function(req, res) {
	  		user = req.user.toJSON()
	    	sockets.pushToSockets({message:'news', payload:user});
	    	if(user.facebook)
	    		profile = user.facebook
	    		res.render('account', { user: profile });
	});

	app.get('/auth/google',
  		passport.authenticate('google', { scope: 'https://www.googleapis.com/auth/plus.login' }));

	app.get('/auth/google/callback',
	  passport.authenticate('google', { failureRedirect: '/' }),
	  function(req, res) {
	    res.redirect('/');
	  });

	app.get('/logout', function(req, res){
	  req.logout();
	  res.redirect('/');
	});

	function ensureAuthenticated(req, res, next) {
	  if (req.isAuthenticated()) { return next(); }
	  res.redirect('/login')
	}
};