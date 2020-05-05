#!/usr/bin/node

const argument = process.argv[2];
let myMessage = 'Not a number';
if (isNaN(Number(argument))) {
  console.log(myMessage);
} else {
  myMessage = 'My number: ' + parseInt(argument);
  console.log(myMessage);
}
