#!/usr/bin/node

const process = require('process');

const myNum = parseInt(process.argv[2]);

function fact (num) {
  if (num === 1) {
    return 1;
  }
  return num * fact(num - 1);
}

if (!myNum) {
  console.log(1);
} else {
  console.log(fact(myNum));
}
