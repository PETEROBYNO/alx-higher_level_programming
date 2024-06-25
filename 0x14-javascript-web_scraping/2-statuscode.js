#!/usr/bin/node

const request = require('request');

const url = process.argv[2]; // Get the URL from the command line arguments

// Make a GET request to the URL
request.get(url, (error, response) => {
  if (error) {
    console.error(error); // Print the error if it occurred
  } else {
    console.log(`code: ${response.statusCode}`); // Print the status code
  }
});
