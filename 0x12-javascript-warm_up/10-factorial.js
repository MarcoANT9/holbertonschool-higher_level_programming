#!/usr/bin/node

function factorial (n) {
  if (n === 1 || isNaN(n)) {
    return 1;
  }
  const fact = n * factorial(n - 1);
  return fact;
}

console.log(factorial(process.argv[2]));
