#!/usr/bin/node

const request = require('request');

// syntax: https://swapi-api.hbtn.io/api/films/{user input}, get title

// const episode = process.argv[2];
// const url = 'https://swapi-api.hbtn.io/api/films/'.concat(episode);
const url = 'https://swapi-api.hbtn.io/api/people/18';
request(url, function (error, response, body) {
  if (error) throw error;
  const movies = JSON.parse(body).films;
  console.log(movies.length);
});
