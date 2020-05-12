#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url.concat(process.argv[2]), function (error, response) {
  if (error) {
    console.error(error);
  }
  const body = JSON.parse(response.body);
  console.log(body.title);
});
