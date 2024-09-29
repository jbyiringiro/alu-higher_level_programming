#!/usr/bin/node

const array = require('./100-data.js').list;
const newArray = array.map((data, index) => index * data);
console.log(array);
console.log(newArray);
