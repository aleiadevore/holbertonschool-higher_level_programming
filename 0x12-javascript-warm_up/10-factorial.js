#!/usr/bin/node
const a = parseInt(process.argv[2]);

if (isNaN(a)) {
  console.log(1);
} else {
  console.log(factorial(a));
}
function factorial (a) {
  if (a < 0) {
    return -1;
  } else if (a === 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
}
