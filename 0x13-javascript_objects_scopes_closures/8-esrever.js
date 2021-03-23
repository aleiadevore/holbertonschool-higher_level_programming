#!/usr/bin/node
exports.esrever = function (list) {
  const newlist = [];
  let i = 0;
  let j = list.length - 1;

  for (; j >= 0; j--, i++) {
    newlist[i] = list[j];
  } return newlist;
};
