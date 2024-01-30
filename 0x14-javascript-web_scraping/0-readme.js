#!/usr/bin/node
/**
 * Read the content of a file in asynchrounous way
 */
const fs = require('fs');

const nameOfFile = process.argv[2];

fs.readFile(nameOfFile, { encoding: 'utf8' }, (err, data) => {
  if (err) console.log(err);
  else {
    console.log(data);
  }
});
