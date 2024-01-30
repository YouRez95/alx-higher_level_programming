#!/usr/bin/node
/**
 * make request and prints all characters of a Star Wars movie
 */

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      request(character, (err, res, body) => {
        if (err) console.log(err);
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
