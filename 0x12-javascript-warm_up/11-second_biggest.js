#!/usr/bin/node

const { argv } = require('process');

function secondBiggest (numbers) {
  let bigg = numbers[2] > numbers[3] ? numbers[2] : numbers[3];
  let secBigg = numbers[2] > numbers[3] ? numbers[3] : numbers[2];
  let pointer = 4;
  while (numbers[pointer]) {
    if (parseInt(numbers[pointer]) > parseInt(bigg)) {
      secBigg = bigg;
      bigg = numbers[pointer];
    } else if (parseInt(numbers[pointer]) > parseInt(secBigg)) {
      secBigg = numbers[pointer];
    }
    pointer++;
  }

  return parseInt(secBigg);
}

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  console.log(secondBiggest(argv));
}
