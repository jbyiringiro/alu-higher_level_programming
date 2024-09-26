#!/usr/bin/node
const argv = process.argv.slice(2);
const output = argv[0] ? argv[0] : 'No argument';
console.log(output);
