#!/usr/bin/node
if (process.argv.length <= 3) {
    console.log(0);
  } else {
    const list = process.argv
      .slice(2)
      .map(element => parseInt(element));
    list.splice(
      list.findIndex(
        element => element === Math.max(...list)
      ),
      1
    );
    const secondLargest = Math.max(...list);
    console.log(secondLargest);
  }