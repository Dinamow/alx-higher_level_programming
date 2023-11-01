#!/usr/bin/node

const fs = require('fs');
const FILE_NAME = process.argv[2];
const TEXT = process.argv[3];

fs.writeFile(FILE_NAME, TEXT, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
