$(document).ready(function()
{


    $("#audit_button").click(function(){

        var audit_data=$("#audit_text").val();

        $.ajax({
            url: "/audit_parse",async:true,type: "post",data: { "audit_data":audit_data},
            success: function(response){

            $("#audit_parsed").val(response);
             $("#audit_parsed_div").show()

            }

        });

    });


    $("#upload_audit_button").click(function(){

        var audit_data=$("#audit_fileupload")[0].files[0]
        formdata = new FormData()
        formdata.append("audit_data",audit_data)

        $.ajax({
            url: "/audit_file_parse",async:true,type: "post", data: formdata,contentType: false, processData: false,
            success: function(response){

            $("#audit_parsed").val(response);
             $("#audit_parsed_div").show()

            }

        });

    });


});
