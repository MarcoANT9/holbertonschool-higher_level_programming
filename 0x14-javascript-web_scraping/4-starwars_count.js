#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, response) {
  if (err) {
    console.error(err);
  } else {
    let counter = 0;
    const body = JSON.parse(response.body);
    for (const movies of body.results) {
      for (const actors of movies.characters) {
        if (actors.endsWith('/18/')) {
          counter += 1;
        }
      }
    }
    console.log(counter);
  }
});
