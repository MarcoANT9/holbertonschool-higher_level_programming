#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response) {
  if (error) {
    console.error(error);
  }
  const usersJson = {};
  const body = JSON.parse(response.body);
  for (const task of body) {
    if (task.completed) {
      if (usersJson[task.userId]) {
        usersJson[task.userId] += 1;
      } else {
        usersJson[task.userId] = 1;
      }
    }
  }
  console.log(usersJson);
});
