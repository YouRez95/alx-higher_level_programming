#!/usr/bin/node
/**
 * make request and print the number of movies where the character “Wedge Antilles” is present
 */

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fileName = process.argv[3];
request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(fileName, body, 'utf-8', (err) => {
      if (err) console.log(err);
    });
  }
});
