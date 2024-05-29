// import * as $ from 'jquery';

$(document).ready(function () {
	fetch("https://swapi-api.alx-tools.com/api/people/5/?format=json")
		.then(response => {
			if (!response.ok) {
				throw Error(response.statusText);
			}
			return response.json();
		}).then(data => {
			$("DIV#character").text(data.name);
		}).catch(error => {
			console.log(error);
		});
});
