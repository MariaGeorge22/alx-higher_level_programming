#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const fileAContents = fs.readFileSync(fileA);
const fileBContents = fs.readFileSync(fileB);

fs.writeFile(fileC, fileAContents + fileBContents, err => {
  if (err) {
    console.error(err);
  }
});
