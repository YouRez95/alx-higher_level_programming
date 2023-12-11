#!/usr/bin/node

const process = require('process');

const myNumber = parseInt(process.argv[2]);

if (!myNumber) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < myNumber; i++) {
    console.log('C is fun');
  }
}
