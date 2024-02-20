$(document).ready(function()
{



    $("#upload_vizoozie_button").click(function(){

        var vizoozie_data=$("#vizoozie_fileupload")[0].files[0]
        var filename = vizoozie_data.name
        formdata = new FormData()
        formdata.append("vizoozie_data",vizoozie_data)
        var xhrOverride = new XMLHttpRequest();
        // tell it you want an ArrayBuffer
        xhrOverride.responseType = 'arraybuffer';

        $.ajax({
            url: "/vizoozie_file_parse",async:true,type: "post", data: formdata,contentType: false, processData: false,
            xhr: function() { return xhrOverride; }, success: function(response){

//                console.log(response)



                    var blob=new Blob([response],{type: 'application/octetstream'});
                    var link=document.createElement('a');
                    link.href=window.URL.createObjectURL(blob);
                    link.download=filename+".pdf";
                    link.click();

            }

        });

    });


});
