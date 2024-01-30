#!/usr/bin/node
/**
 * make request and  computes the number of tasks completed by user id
 */

const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    const response = JSON.parse(body);
    const completedTask = {};
    for (const user of response) {
      const userId = user.userId;
      if (user.completed === true) {
        if (!(userId in completedTask)) completedTask[userId] = 1;
        else completedTask[userId] += 1;
      }
    }
    console.log(completedTask);
  }
});
