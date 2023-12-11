#!/usr/bin/node

const process = require('process');

const firstNum = parseInt(process.argv[2]);
const secondNum = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(firstNum, secondNum));
