#!/usr/bin/node

const request = require('request');

// syntax: https://swapi-api.hbtn.io/api/films/{user input}, get title

const episode = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/'.concat(episode);

request(url, function (error, response, body) {
  if (error) throw error;
  console.log(JSON.parse(body).title);
});
