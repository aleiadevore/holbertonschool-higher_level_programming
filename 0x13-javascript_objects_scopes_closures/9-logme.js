#!/usr/bin/node
let calls = 0;
exports.logMe = function (item) {
  calls++;
  console.log(calls + ': ' + item);
};
