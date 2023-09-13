#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    const printChar = c || 'X';
    for (let i = 0; i < this.width; i++) {
      console.log(printChar.repeat(this.height));
    }
  }
};
