#!/usr/bin/node
let large = 0;
let ans = 0;
let i = 2;

if (process.argv.length <= 3) {
  console.log(0);
} else {
  large = process.argv[2];
  for (; process.argv[i] != null; i++) {
    if (isNaN(process.argv[i])) {
      continue;
    } else if (large >= ans) {
      ans = large;
      large = parseInt(process.argv[i]);
    }
  } console.log(ans);
}
