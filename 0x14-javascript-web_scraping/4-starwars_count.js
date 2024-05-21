#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(
	  process.argv[2],
	  (error, response, body) => {
		      if (error) {
			            log(error);
			          } else if (response.statusCode !== 200) {
					        console.log('An error occured. Status code: ' + response.statusCode);
					      } else {
						            let count = 0;
						            const id = 18;
						            const movies = (JSON.parse(body)).results;
						            for (const index in movies) {
								            const movie = movies[index];
								            const characters = movie.characters;
								            for (const char in characters) {
										              if (characters[char].includes(id)) {
												                  count++;
												                }
										            }
								          }
						            log(count);
						          }
		    }
);
