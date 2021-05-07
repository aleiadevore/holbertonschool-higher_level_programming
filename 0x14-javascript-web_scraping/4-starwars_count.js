#!/usr/bin/node

const request = require('request');

// syntax: https://swapi-api.hbtn.io/api/films/{user input}, get title

const url = process.argv[2];
let count = 0;

// const url = 'https://swapi-api.hbtn.io/api/people/18';
request(url, function (error, response, body) {
  if (error) throw error;
  const movies = JSON.parse(body).results;
  for (const i in movies) {
    for (const char in movies[i].characters) {
      if (movies[i].characters[char].includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
