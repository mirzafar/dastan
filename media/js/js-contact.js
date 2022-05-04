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
                     $('.js-scf').css("display","block");
                     $('.js-scf').text("Сатти жиберилди!!!");
                     myFunction();
                     $(window).click(function (){
                        location.reload()
                     })
                 }else{
                     var errors = d['errors'];
                     $('.js-err').css("display","block");
                     $('.js-err').text(errors);
                     myFunction();
                 }
             },
             error: function (d){
                 $('.js-err').css("display","block");
                 $('.js-err').text("Агылшынша толдырынгыз");
             }
         });
    });

})