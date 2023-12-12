#!/usr/bin/node

exports.callMeMoby = (num, callback) => {
  for (let i = 0; i < num; i++) {
    callback();
  }
};
