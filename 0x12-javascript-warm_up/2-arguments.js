#!/usr/bin/node

const lengtVars = process.argv.length;
let myVar = 'No argument';
if (lengtVars === 2) {
  console.log(myVar);
} else if (lengtVars === 3) {
  myVar = 'Argument found';
  console.log(myVar);
} else {
  myVar = 'Arguments found';
  console.log(myVar);
}
