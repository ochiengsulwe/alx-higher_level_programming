#!/usr/bin/node
const i = parseInt(process.argv[2]);
if (!isNaN(i)) {
  for (let y = 0; y < i; y++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
