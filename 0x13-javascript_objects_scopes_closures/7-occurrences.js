#!/usr/bin/node

exports.nbOccurences = (list, searchElement) => {
  let i = 0;
  let counter = 0;
  while (list[i]) {
    if (list[i] === searchElement) {
      counter++;
    }
    i++;
  }
  return counter;
};
