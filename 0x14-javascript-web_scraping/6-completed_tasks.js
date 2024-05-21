#!/usr/bin/node
const { log } = require('console');
const request = require('request');

request(
	  process.argv[2],
	  (error, response, body) => {
		      if (error) {
			            log(error);
			          } else {
					        const completedUsers = {};
					        const tasks = JSON.parse(body);
					        for (const index in tasks) {
							        const user = tasks[index].userId;
							        if (tasks[index].completed) {
									          completedUsers[user] = (completedUsers[user] || 0) + 1;
									        }
							      }
					        log(completedUsers);
					      }
		    }
);
