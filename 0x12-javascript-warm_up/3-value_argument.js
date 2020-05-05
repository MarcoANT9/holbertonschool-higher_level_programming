#!/usr/bin/node

const argument = process.argv[2];
const myVar = 'No argument';
if (!argument) {
  console.log(myVar);
} else {
  console.log(argument);
}
