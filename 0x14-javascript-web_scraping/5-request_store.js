#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const URL = process.argv[2];
const FILENAME = process.argv[3];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(FILENAME, body, 'utf8', (err) => {
      if (err) console.error(err);
    });
  }
});
