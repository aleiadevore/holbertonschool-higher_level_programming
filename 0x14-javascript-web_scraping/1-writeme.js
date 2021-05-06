#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
const input = process.argv[3];

fs.writeFile(filename, input, 'utf8', function (err) {
  if (err) throw err;
});
