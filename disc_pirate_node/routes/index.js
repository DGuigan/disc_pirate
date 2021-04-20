var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/albums', function (req, res) {
  res.render('albums', { title: 'All Albums'});
});

module.exports = router;
