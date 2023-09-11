#!/usr/bin/node

const args = process.argv;

if (isNaN(parseInt(args[2])) || isNaN(parseInt(args[3]))) {
  console.log('NaN');
} else {
  console.log(`${parseInt(args[2]) + parseInt(args[3])}`);
}
