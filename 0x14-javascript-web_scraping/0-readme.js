#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line arguments

// Read the file asynchronously in utf-8 encoding
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print the error if it occurred
  } else {
    console.log(data); // Print the content of the file
  }
});
