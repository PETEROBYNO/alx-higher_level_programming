#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the command line arguments

// Make a GET request to the specified URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error); // Print the error if it occurred
  } else {
    const todos = JSON.parse(body);

    // Filter completed tasks and count them for each user
    const completedTasksByUser = todos.reduce((countByUser, todo) => {
      if (todo.completed) {
        countByUser[todo.userId] = (countByUser[todo.userId] || 0) + 1;
      }
      return countByUser;
    }, {});

    console.log(completedTasksByUser); // Print the result
  }
});
