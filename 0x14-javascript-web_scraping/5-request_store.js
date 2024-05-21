#!/usr/bin/node
const { log } = require('console');
const request = require('request');
const fs = require('fs');

request(
	  process.argv[2],
	  (error, response, body) => {
		      if (error) {
			            log(error);
			          } else {
					        fs.writeFileSync(process.argv[3], body, {
							        encoding: 'utf8'
							      });
					      }
		    }
);
