#!/usr/bin/node
if (process.argv[2] && !isNaN(process.argv[2])) {
    for (
      let index = 0;
      index < parseInt(process.argv[2]);
      index++
    ) {
      console.log('X'.repeat(parseInt(process.argv[2])));
    }
  } else {
    console.log('Missing size');
  }