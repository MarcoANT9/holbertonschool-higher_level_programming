#!/usr/bin/node

const argument = process.argv[2];
const number = parseInt(argument);
if (isNaN(number)) {
  console.log('Missing size');
} else {
  let i = number;
  while (i > 0) {
    console.log('X'.repeat(number));
    i--;
  }
}
