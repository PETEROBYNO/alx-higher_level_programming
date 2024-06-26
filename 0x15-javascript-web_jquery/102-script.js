$(document).ready(function() {
    // When the user clicks on INPUT#btn_translate
    $("#btn_translate").click(function() {
        // Get the entered language code from INPUT#language_code
        var languageCode = $("#language_code").val();

        // Fetch the translation using the API
        $.get("https://www.fourtonfish.com/hellosalut/hello/", { lang: languageCode }, function(data) {
            // Display the translation in DIV#hello
            $("#hello").text(data.hello);
        });
    });
});

