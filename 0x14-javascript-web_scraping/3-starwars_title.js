#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]; // Get the movie ID from the command line arguments
const apiURL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(apiURL, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if it occurred
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title); // Print the title of the movie
  }
});
