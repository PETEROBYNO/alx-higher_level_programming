$(function () {
	var Hello = $("#character");

	$.ajax({
		type: "GET",
		url: "https://hellosalut.stefanbohacek.dev/?lang=fr",
		success: function(data) {
			$(data.hello).appendTo(Hello);
		};
	});
});
