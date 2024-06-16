#!/usr/bin/node

const process = require('process');
const args = process.argv.slice(2);

const numOccurrences = parseInt(args[0]);

if (!isNaN(numOccurrences)) {
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missign number of occurrences');
}
