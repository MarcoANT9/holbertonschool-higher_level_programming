#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, response) {
  if (err) {
    console.error(err);
  } else {
    let counter = 0;
    const actor = 'https://swapi-api.hbtn.io/api/people/18/';
    let body = JSON.parse(response.body);
    body = body.results;
    for (let index = 0; index < body.length; index++) {
      const movie = body[index];
      const actors = movie.characters;
      for (let jndex = 0; jndex < actors.length; jndex++) {
	if (actors[jndex] === actor) {
          counter++;
	}
      }
    }
    console.log(counter);
  }
});
