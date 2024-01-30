#!/usr/bin/node
/**
 * make request and print the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');

const url = process.argv[2];
request(url, (err, response, body) => {
  if (err) console.log(err);
  else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const film of results) {
      for (const character of film.characters) {
        if (character.includes('18')) count += 1;
      }
    }
    console.log(count);
  }
});
