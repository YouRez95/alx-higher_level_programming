#!/usr/bin/node
/**
 * Write text to file in synchronous way
 */

const fs = require('fs');
const filePath = process.argv[2];
const textToWrite = process.argv[3];
try {
  fs.writeFileSync(filePath, textToWrite, { encoding: 'utf-8' });
} catch (err) {
  console.log(err);
}
