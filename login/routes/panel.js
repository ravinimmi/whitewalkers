var express = require('express');
var router = express.Router();

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/frame-questions', function(req, res, next) {
  res.render('panel/frame_questions', { layout: false });
});

router.get('/choose-users', function(req, res, next) {
  res.render('panel/choose_users', { layout: false });
});

router.get('/pay-n-roll', function(req, res, next) {
  res.render('panel/pay_n_roll', { layout: false });
});

router.get('/templates', function(req, res, next) {
  res.render('panel/templates', { layout: false });
});

router.get('/template', function(req, res, next) {
	if(req.params.choice == 'single_choice')
  		res.render('panel/single_choice', { layout: false });
  	else if(req.params.choice == 'multiple_choice')
  		res.render('panel/multiple_choice', { layout: false });
  	else if(req.params.choice == 'image_choice')
  		res.render('panel/rating_choice', { layout: false });
});

module.exports = router;
