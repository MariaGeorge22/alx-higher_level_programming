#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(
	  `https://swapi-api.alx-tools.com/api/films/${process
		      .argv[2]}`,
	  (error, response, body) => {
		      if (error) {
			            log(error);
			          }
		      log(JSON.parse(body).title);
		    }
);
