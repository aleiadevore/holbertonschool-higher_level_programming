#!/usr/bin/node
const inpt = process.argv[2];
let i;

if (isNaN(inpt)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < parseInt(inpt); i++) {
    console.log('C is fun');
  }
}
