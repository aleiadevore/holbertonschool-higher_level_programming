#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) throw error;
  console.log('code:', response && response.statusCode); // Print the response status code if a response was received
});
