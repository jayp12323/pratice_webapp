$(document).ready(function()
{



    $("#upload_revisions_button").click(function(){

        var revisions_data=$("#revisions_fileupload")[0].files[0]
        formdata = new FormData()
        formdata.append("revisions_data",revisions_data)

        $.ajax({
            url: "/revisions_file_parse",async:true,type: "post", data: formdata,contentType: false, processData: false,
            success: function(response){

                console.log(response)



                    var blob=new Blob([response]);
                    var link=document.createElement('a');
                    link.href=window.URL.createObjectURL(blob);
                    link.download="revisions.csv";
                    link.click();

            }

        });

    });


});
