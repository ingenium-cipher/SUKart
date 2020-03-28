var pk

$(document).ready(function(){
    pk = window.location.href.split('/')[4]

    $.ajax({
        type: 'GET',
        url: '/api/product/' + pk,
        dataType: 'json',
        success: function(data){
                $('.image').append('\
                <img src="'+ data.image +'"/> \
            ')
        }
    });

});
