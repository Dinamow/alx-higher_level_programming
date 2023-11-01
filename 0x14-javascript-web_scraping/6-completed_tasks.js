#!/usr/bin/node

const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const TODOS = {};
    const RESULTS = JSON.parse(body);
    RESULTS.map((task) => {
      if (!Object.prototype.hasOwnProperty.call(TODOS, '' + task.userId)) {
        if (task.completed) TODOS['' + task.userId] = 0;
      }
      if (task.completed) TODOS['' + task.userId] += 1;
      return task;
    });
    console.log(TODOS);
  }
});
