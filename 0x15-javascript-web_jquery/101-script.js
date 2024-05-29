// import * as $ from 'jquery';

const list = 'UL.my_list';
const item = '<li>Item</li>';
const addElement = 'DIV#add_item';
const removeElement = 'DIV#remove_item';
const clearElement = 'DIV#clear_list';
$(document).ready(function () {
	$(addElement).click(function () {
		$(list).append(item);
	});
	$(removeElement).click(function () {
		$(`${list} li:last-child`).remove();
	});
	$(clearElement).click(function () {
		$(list).empty();
	});
});
