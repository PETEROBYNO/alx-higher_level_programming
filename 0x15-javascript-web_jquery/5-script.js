$(function() {
	$("#add_item").click(function() {
		var newItem = $("<li>Item</li>");
		$("UL.my_list").append(newItem);
	});
});
