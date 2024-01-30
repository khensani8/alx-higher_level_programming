#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const string = process.argv[3];

fs.writeFile(file, string, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('File has been successfully written.');
  }
});
