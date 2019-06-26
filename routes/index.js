var express = require('express');
var router = express.Router();

let config = require('../config.json');
const fs = require('fs');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'PiPot' });
});

router.get('/table', function(req, res, next){
  res.render('table',{ title: 'PiPot', users: [{name: "Mark", password:"1234567890"}, {name:"Otto", password:"qwerty" }] });
});

router.get('/config', function(req, res, next){
  res.render('config', { title: 'PiPot', networks: ["Network 1", "Network 2", "Network 3", "Network 4"]});
});

router.post('/config', function(req, res, next){
  config["save-password"] = req.body['save-password'];
  config["show-password"] = req.body['show-password'];
  fs.writeFileSync('../config.json', config);
  console.log(req.body);
  res.render('config', { title: 'PiPot', networks: ["Network 1", "Network 2", "Network 3", "Network 4"]});
});

module.exports = router;
