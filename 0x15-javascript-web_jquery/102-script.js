// import * as $ from 'jquery';

const languageCode = 'INPUT#language_code';
const btn = 'INPUT#btn_translate';
const helloElement = 'DIV#hello';
const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
$(document).ready(function () {
	$(btn).click(function () {
		$.get(`${url}${$(languageCode).val()}`).then((data) => {
			$(helloElement).text(data.hello);
		})
	});
});
