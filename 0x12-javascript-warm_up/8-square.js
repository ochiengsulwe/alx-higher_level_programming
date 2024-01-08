#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row.trim()); // Removing trailling whitespaces in each line
  }
} else {
  console.log('Missing size');
}
