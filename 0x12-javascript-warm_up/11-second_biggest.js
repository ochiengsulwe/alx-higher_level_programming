#!/usr/bin/node

function findSecondBiggest (nums) {
  const numbers = nums.map(Number);

  if (numbers.length <= 1) {
    return 0;
  }

  const sortedNumbers = numbers.sort((a, b) => b - a);
  return sortedNumbers[1];
}

const args = process.argv.slice(2);
const secondBiggest = findSecondBiggest(args);
console.log(secondBiggest);
