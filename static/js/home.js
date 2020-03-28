$(document).ready(function(){
    $.ajax({
        type: 'GET',
        url: '/api/product_list/',
        dataType: 'json',
        success: function(data){
            $.each(data, function(index, product){
                url_detail = '/product/' + product.id;
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
