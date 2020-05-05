#!/usr/bin/node
const args = process.argv;
const lenArgs = process.argv.length;
if (lenArgs <= 3) {
  console.log(0);
} else {
  args.sort(function(a, b) { return a - b });
  console.log(args[lenArgs - 2]);
}
