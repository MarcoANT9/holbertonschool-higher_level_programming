#!/usr/bin/node

const array = require('./100-data.js').list;
const map1 = array.map(function multiply (x, index) { return (x * index); });
console.log(array);
console.log(map1);
