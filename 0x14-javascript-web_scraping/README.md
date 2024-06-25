# Javascript - Web scraping

# Learning Objectives

* How to manipulate JSON data
* How to use `request` and fetch API
* How to read and write a file using `fs` module

# Tasks

## Readme

Write a script that reads and prints the content of a file.

* The first argument is the file path
* The content of the file must be read in `utf-8`
* If an error occurred during the reading, print the error object

**Solution:** [0-readme.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/0-readme.js)


## Write me

Write a script that writes a string to a file.

* The first argument is the file path
* The second argument is the string to write
* The content of the file must be written in `utf-8`
* If an error occurred during while writing, print the error object

**Solution:** [1-writeme.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/1-writeme.js)


## Status code

Write a script that display the status code of a `GET` request.

* The first argument is the URL to request (`GET`)
* The status code must be printed like this: `code: <status code>`
* You must use the module `requests`

**Solution:** [2-statuscode.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/2-statuscode.js)

## Star wars movie title

Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

* The first argument is the movie ID
* You must use the [Star wars API](https://swapi-api.hbtn.io/) with the endpoint `https://swapi-api.hbtn.io/api/films/:id`
* You must use the module `requests`

**Solution:** [3-starwars_title.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/3-starwars_title.js)



## Star wars Wedge Antilles

Write a script that prints the number of movies where the character “Wedge Antilles” is present.

* The first argument is the API URL of the [Star wars API](https://swapi-api.hbtn.io/): `https://swapi-api.hbtn.io/api/films/`
* Wedge Antilles is character ID `18`
* You must use the module `requests`

**Solution:** [4-starwars_count.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/4-starwars_count.js)



## Loripsum

Write a script that gets the contents of a webpage and stores it in a file.

* The first argument is the URL to request
* The second argument the file path to store the body response
* The file must be UTF-8 encoded
* You must use the module `requests`

**Solution:** [5-request_store.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/5-request_store.js)

## How many completed?

Write a script that computes the number of tasks completed by user id.

* The first argument is the API URL: `https://jsonplaceholder.typicode.com/todos`
* You must use the module `requests`

**Solution:** [6-completed_tasks.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/6-completed_tasks.js)


## Who was playing in this movie?

Write a script that prints all characters of a Star Wars movie:

* The first argument is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name by line
* You must use the [Star wars API](https://swapi-api.hbtn.io/)
* You must use the module `requests`

**Solution:** [100-starwars_characters.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/100-starwars_characters.js)



## Right order

Write a script that prints all characters of a Star Wars movie:

* The first argument is the Movie ID - example: `3` = “Return of the Jedi”
* Display one character name by line **in the same order of the list “characters” in the** `/films/` **response**
* You must use the [Star wars API](https://swapi-api.hbtn.io/)
* You must use the module `requests`

**Solution:** [101-starwars_characters.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/101-starwars_characters.js)


## Twitter Auth

Write a Javascript script that takes in 3 strings and sends a search request to the [Twitter API](https://developer.twitter.com/en/docs/api-reference-index)

* Use the [Twitter API search endpoint](https://developer.twitter.com/en/docs/api-reference-index)
* Use the [Application-only authentication](https://developer.twitter.com/en/docs/basics/authentication/overview) flow to do a search request
* Create an Twitter application [here](https://developer.twitter.com/app)
* The first argument must be the Consumer Key (API Key)
* The second argument must be the Consumer Secret (API Secret)
* The third argument must be the search string
* Display only 5 results in the following format: `[<Tweet ID>] <Tweet text> by <Tweet owner name>` (see example below)
* Only these modules are allowed: `requests`, `base-64` and `utf8`
* You don’t need to check arguments passed to the script (number or type)

**Solution:** [102-search_twitter.js](https://github.com/just337ine/alx-higher_level_programming/blob/main/0x14-javascript-web_scraping/102-search_twitter.js)
