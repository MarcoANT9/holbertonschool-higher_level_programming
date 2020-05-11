#!/usr/bin/node

// Counts the number of ocurrences of an element in a list.
exports.esrever = function (list) {
  const newArray = [];
  for (let i = 0; i < list.length; ++i) {
    newArray.push(list[list.length - 1 - i]);
  }
  return newArray;
};
