#!/usr/bin/node

if (isNaN(Number(process.argv[2]))) {
  console.log('Missing number of ocurrences');
} else {
  let ocurrences = Number(process.argv[2]);
  while (ocurrences > 0) {
    console.log('C is cool');
    ocurrences--;
  }
}
