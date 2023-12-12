#!/usr/bin/node

exports.addMeMaybe = (num, callback) => {
  num = num + 1;
  callback(num);
};
