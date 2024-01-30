#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const API_URL = https://swapi-api.alx-tools.com/api/films/:id;

request(API_URL + movieID, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response .statusCode === 200) {
    const repsonseJSON= JSON.parse(body);
    console.log(responeJSON.title);
  } else {
  console.log('Error Code' + response.statusCode);
  }
});
