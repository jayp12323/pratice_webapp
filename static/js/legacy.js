$(document).ready(function () {


    $("#legacy_button").click(function () {

        var legacy_data = $("#legacy_text").val();

        $.ajax({
            url: "/legacy_return",
            async: true,
            type: "post",
            data: {
                "legacy_data": legacy_data
            },
            success: function (response) {
//                $("#legacy_parsed").val(response);
                if (response == "notfound"){
                    $("#legacy_parsed").html('Cannot find Cloudera case with LHWX Case # '+legacy_data);
                }
                else if (response == "notcorrect"){
                    $("#legacy_parsed").html('Case entered is not a valid case syntax');
                }
                else{
                    var link = "https://csh.cloudera.com/ccs/index.html#/case/"+response+"/case-details"
                    $("#legacy_parsed").html('New Cloudera case is: <a href="'+link+'" target="_blank">'+response+'</a>');
                }
                $("#legacy_parsed").show()


            }

        });


    });

    $("#upload_legacy_button").click(function () {

        var legacy_data=$("#legacy_fileupload")[0].files[0]
        formdata = new FormData()
        formdata.append("legacy_data",legacy_data)

        $.ajax({
            url: "/legacy_parse_file",
            async: true,
            type: "post",
            data: formdata,contentType: false, processData: false,
            success: function (response) {

                $("#legacy_parsed").val(response);
                $("#legacy_parsed_div").show()

            }


        });


    });


});