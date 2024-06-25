#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2]; // Get the file path from the command line arguments
const content = process.argv[3]; // Get the string to write from the command line arguments

// Write the content to the file asynchronously in utf-8 encoding
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err); // Print the error if it occurred
  }
});
