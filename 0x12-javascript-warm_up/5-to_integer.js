#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);
const number = parseInt(args[0]);

// Checking of the conversion is successful
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
