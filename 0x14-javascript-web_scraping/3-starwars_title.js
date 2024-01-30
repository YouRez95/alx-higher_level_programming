#!/usr/bin/node
/**
 * make request and get the title of the film
 */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
