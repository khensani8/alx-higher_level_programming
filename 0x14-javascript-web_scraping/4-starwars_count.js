#!/usr/bin/node

const request = require('request')

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 4-wedges_movies.js <API-URL>');
  process.exit(1);
}

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    try {
      // Parse the JSON response
      const filmsData = JSON.parse(body);

      // Filter movies where "Wedge Antilles" is present
      const wedgeMovies = filmsData.results.filter(movie => {
        return movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/');
      });

      // Print the number of movies where Wedge Antilles is present
      console.log(`Number of movies with Wedge Antilles: ${wedgeMovies.length}`);
    } catch (parseError) {
      console.error('Error parsing JSON response:', parseError);
    }
  }
});
