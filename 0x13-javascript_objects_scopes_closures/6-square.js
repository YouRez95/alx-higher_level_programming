#!/usr/bin/node

const SquareParent = require('./5-square');

class Square extends SquareParent {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        const char = [];
        for (let i = 0; i < this.width; i++) {
          char.push(c);
        }
        console.log(char.join(''));
      }
    }
  }
}

module.exports = Square;
