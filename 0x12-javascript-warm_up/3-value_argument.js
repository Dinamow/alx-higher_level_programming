#!/usr/bin/node

const args = process.argv.slice(2);
x = 0;
for (y in args) {
  x++;
}
if (x === 0) {
  console.log('No argument');
} else {
  console.log(args[0]);
}
