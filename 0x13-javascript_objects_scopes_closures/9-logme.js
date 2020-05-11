#!/usr/bin/node

let arg = 0;

// Counts the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  console.log(arg + ': ' + item);
  arg++;
};
