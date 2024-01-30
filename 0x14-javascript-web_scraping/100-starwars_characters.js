#!/usr/bin/node
/**
 * make request and prints all characters of a Star Wars movie in order
 */

const request = require('request');

const urlFilms = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) reject(err);
      else resolve(JSON.parse(body));
    });
  });
}

async function printCharacter () {
  try {
    const responseMovies = await makeRequest(urlFilms);
    for (const character of responseMovies.characters) {
      const responseCharacter = await makeRequest(character);
      console.log(responseCharacter.name);
    }
  } catch (err) {
    console.log(err);
  }
}

printCharacter();
