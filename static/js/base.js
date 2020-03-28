function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



$(document).ready(function(){

    $('.search_button').click(function(event){
        event.preventDefault();
        let search_string = $('.search_product').val();

        $.ajax({
            type: 'POST',
            url: '/api/product_search',
            data: {'search_string': search_string},
            dataType: 'json',
            success: function(data){
                $('.tiles').html("");
                $.each(data, function(index, product){
                    let url_detail = '/product/' + product.id;
                    $('.tiles').append('\
                    <article class="style'+index+1+'">\
                        <span class="image">\
                            <img src="'+ product.image +'"/> \
                        </span>\
                        <a href="'+url_detail+'">\
                            <div class="content">\
                                <p>'+product.description+'</p>\
                            </div>\
                        </a><br>\
                        <div>\
                        <h2>'+product.title+'</h2><br><h6>'+product.company+'</h6><br>\
                        <h4> Rs '+product.price+'</h4>\
                        </div>\
                    </article>\
                    ')
                });
            }
        });
    });


});
