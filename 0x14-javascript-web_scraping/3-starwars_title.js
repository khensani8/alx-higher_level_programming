#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 3-starwars_title.js <movie-ID>');
  process.exit(1);
}

// Get the movie ID from the command line argument
const movieID = process.argv[2];

// Make a GET request to the Star Wars API
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      // Parse the JSON response
      const movieData = JSON.parse(body);

      // Print the title of the movie
      console.log(movieData.title);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
