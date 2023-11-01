#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];
const ID = '/people/18';

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const RESULT = JSON.parse(body).results;
    let totale = 0;
    RESULT.map((movie) => {
      const HASCHAR = movie.characters.some(url => url.includes(ID));
      if (HASCHAR) totale += 1;
      return movie;
    });
    console.log(totale);
  }
});
