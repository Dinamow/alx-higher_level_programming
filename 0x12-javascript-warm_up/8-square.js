#!/usr/bin/node

const args = process.argv;

if (isNaN(parseInt(args[2]))) {
  console.log('Missing size');
} else if (parseInt(args[2]) > 0) {
  for (let i = 0; i < parseInt(args[2]); i++) {
    for (let i = 0; i < parseInt(args[2]); i++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
