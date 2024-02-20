$(document).ready(function()
{


    $("#dotpdf_button").click(function(){

        var dotpdf_data=$("#dotpdf_text").val();
        formdata = new FormData()
        formdata.append("dotpdf_data",dotpdf_data)
        var xhrOverride = new XMLHttpRequest();
        // tell it you want an ArrayBuffer
        xhrOverride.responseType = 'arraybuffer';

        $.ajax({
            url: "/dotpdf_parse",async:true,type: "post", data: formdata,contentType: false, processData: false,
            xhr: function() { return xhrOverride; }, success: function(response){

//                console.log(response)



                    var blob=new Blob([response], { type: 'application/pdf' });
                    PDFObject.embed(window.URL.createObjectURL(blob), "#dotpdf_pdf");

            }

        });

    });

});
