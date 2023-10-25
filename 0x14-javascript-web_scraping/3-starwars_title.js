#!/usr/bin/node

const request = require('request');
const ID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
