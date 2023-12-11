#!/usr/bin/node

const process = require('process');

const myNumber = parseInt(process.argv[2]);

if (!myNumber) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myNumber; i++) {
    console.log('X'.repeat(myNumber));
  }
}
