#!/usr/bin/node

const fs = require('fs');
const FILE_NAME = process.argv[2];

fs.readFile(FILE_NAME, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
