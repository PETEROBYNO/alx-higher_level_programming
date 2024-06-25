#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2]; // Get the URL from the command line arguments
const filePath = process.argv[3]; // Get the file path from the command line arguments

// Make a GET request to the specified URL
request.get(url, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if it occurred
  } else {
    // Write the body response to the file in UTF-8 encoding
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
