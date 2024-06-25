#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the command line arguments
const characterId = 18; // Wedge Antilles character ID

// Make a GET request to the Star Wars API
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if it occurred
  } else {
    const films = JSON.parse(body).results;

    // Use find to check if Wedge Antilles is present in each movie
    const wedgeMovies = films.reduce((count, film) => {
      return count + (film.characters.find(char => char.includes(`/people/${characterId}/`)) ? 1 : 0);
    }, 0);

    console.log(wedgeMovies); // Print the number of movies
  }
});
