#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const hero = JSON.parse(body).characters;
  exactOrder(hero, 0);
});

const exactOrder = (hero, y) => {
  if (y === hero.length) return;
  request(hero[y], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(hero, y + 1);
  });
};
