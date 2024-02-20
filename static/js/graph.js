$(document).ready(function()
{


$("#graph_button").click(function(){

    var graph_data=$("#graph_data").val();

    $.ajax({
            url: "/graph_data",async:true,type: "post",data: { "graph_data":graph_data},
            success: function(response){



            $("#graph_div").append(response);
            }

            });



});

});
