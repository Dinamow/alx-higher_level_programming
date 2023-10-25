#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  console.log(`code: ${response.statusCode}`);
  if (error) console.error(error);
});
