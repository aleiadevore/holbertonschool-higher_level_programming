#!/usr/bin/node
const SupSquare = require('./5-square');

module.exports = class Square extends SupSquare {
  charPrint (c) {
    let i;
    if (c === undefined) {
      c = 'X';
    } for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
