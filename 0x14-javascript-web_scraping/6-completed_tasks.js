#!/Users/mac/.nvm/versions/node/v16.13.0/bin/node
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
      if (!(userId in completedTask)) completedTask[userId] = 0;
      if (user.completed === true) completedTask[userId] += 1;
    }
    console.log(completedTask);
  }
});
