#!/usr/bin/node

exports.converter = (base) => {
  return (to) => {
    return to.toString(base);
  };
};
