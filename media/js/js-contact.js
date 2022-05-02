$(document).ready(function() {
    $("#form5").submit(function (e) {
        e.preventDefault();
        var serializedData = $(this).serialize();
         $.ajax({
             type: 'POST',
             dataType: 'json',
             url: $("#form5").attr("action"),
             data: serializedData,
             success: function (d) {
                 if(d['status']==true){
                     alert("Данные отправлены!!!");
                     location.reload()
                 }else{
                     var errors = d['errors'];
                     alert(errors);
                 }
             },
             error: function (d){
                 alert("не заполнено");
             }
         });
    });
})