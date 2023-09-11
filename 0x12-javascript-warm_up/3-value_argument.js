#!/usr/bin/node

const args = process.argv;
let massage = 'No argument';

if (args[2]) {
  massage = args[2];
}

console.log(massage);
