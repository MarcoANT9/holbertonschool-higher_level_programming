#!/usr/bin/node

// Transforms a number from base 10 to another base passed as argument.
exports.converter = function (base) {
  return (number) => number.toString(base);
};
