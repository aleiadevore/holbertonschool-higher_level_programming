#!/usr/bin/node
let inpt;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  inpt = process.argv;
  inpt[0] = null;
  inpt[1] = null;
  inpt.sort(function (a, b) { return a - b; });
  console.log(inpt[inpt.length - 2]);
}
