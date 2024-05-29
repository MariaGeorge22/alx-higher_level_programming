// import * as $ from 'jquery';

$(document).ready(function () {
	fetch("https://swapi-api.alx-tools.com/api/films/?format=json")
		.then(response => {
			if (!response.ok) {
				throw Error(response.statusText);
			}
			return response.json();
		}).then(data => {
			data.results.forEach(element => {
				$("UL#list_movies").append(`<li>${element.title}</li>`);
			});
		}).catch(error => {
			console.log(error);
		});
});
