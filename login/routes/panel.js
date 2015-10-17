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

router.get('/reports', function(req, res, next) {
  res.render('panel/reports', { layout: false });
});

module.exports = router;
