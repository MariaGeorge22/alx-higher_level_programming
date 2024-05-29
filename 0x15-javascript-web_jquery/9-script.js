// import * as $ from 'jquery';

$(document).ready(function () {
	fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
		.then(response => {
			if (!response.ok) {
				throw Error(response.statusText);
			}
			return response.json();
		}).then(data => {
			$("DIV#hello").text(data.hello);
		}).catch(error => {
			console.log(error);
		});
});
