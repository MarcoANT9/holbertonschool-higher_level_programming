#!/usr/bin/node

const argument = process.argv[2];
let number = parseInt(argument);
if (isNaN(number)) {
  console.log('Missing number of ocurrences');
} else {
  while (number > 0) {
    console.log('C is fun');
    number--;
  }
}
