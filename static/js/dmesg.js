$(document).ready(function () {


    $("#dmesg_button").click(function () {

        var dmesg_data = $("#dmesg_text").val();

        $.ajax({
            url: "/dmesg_parse",
            async: true,
            type: "post",
            data: {
                "dmesg_data": dmesg_data
            },
            success: function (response) {


                $("#dmesg_parsed").val(response);
                $("#dmesg_parsed_div").show()

            }

        });


    });

    $("#upload_dmesg_button").click(function () {

        var dmesg_data=$("#dmesg_fileupload")[0].files[0]
        formdata = new FormData()
        formdata.append("dmesg_data",dmesg_data)

        $.ajax({
            url: "/dmesg_parse_file",
            async: true,
            type: "post",
            data: formdata,contentType: false, processData: false,
            success: function (response) {

                $("#dmesg_parsed").val(response);
                $("#dmesg_parsed_div").show()

            }


        });


    });


});