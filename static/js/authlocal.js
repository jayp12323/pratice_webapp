$(document).ready(function () {


    $("#authlocal_button").click(function () {

        var principal = $("#principal_text").val();
        var authlocal = $("#authlocal_text").val();

        $.ajax({
            url: "/authlocal_parse",
            async: true,
            type: "post",
            data: {
                "principal": principal,
                "authlocal": authlocal
            },
            success: function (response) {


                $("#authlocal_parsed").val(response);
                $("#authlocal_parsed_div").show()

            }
        });
    });
});