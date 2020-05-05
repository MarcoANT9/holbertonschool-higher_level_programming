#!/usr/bin/node

const args = process.argv.length;
if (args === 2 || args === 3) {
  console.log(0);
} else {
  let index = 0;
  let bigger = process.argv[2];
  let secondBigger = 0;
  while (index < args) {
    console.log(process.argv[index]);
    if (process.argv[index] > bigger) {
      secondBigger = bigger;
      bigger = process.argv[index];
    } else if (process.argv[index] > secondBigger && process.argv[index] < bigger) {
      secondBigger = process.argv[index];
    }
    index++;
  }
  console.log(secondBigger);
}
