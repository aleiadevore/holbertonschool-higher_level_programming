#!/usr/bin/node
exports.converter = function (base) {
  function convert (c) {
    return (c.toString(base));
  } return convert;
};
