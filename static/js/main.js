$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

$(window).resize(function(e) {
    if($(window).width()<=768){
    $("#wrapper").removeClass("toggled");
    }else{
    $("#wrapper").addClass("toggled");
    }
});

$('#addressForm').submit(function(e){
    e.preventDefault()
    var geoCodeRequestCount = $('#geoCodeRCount').attr("count")
    if (geoCodeRequestCount >= 5){ //i.e if the number of free request is less than 5 do not make any new requests..
        address = $('#addressInput').val()
        $('#addressInput').val('')
        $('#locationTitle').text(address)
        $.ajax({
            url: $('#geocode-api').attr('url'),
            method: "POST",
            data: {
                "address":address,
                'csrfmiddlewaretoken': $('#geocode-api').attr('csrf')
            },
            success: function(data){
                $('#lat_li').text(data.lat)
                $('#lng_li').text(data.lng)
                $('#locationTitle').text(data.f_address)
                $('#geoCodeRCount').text(data.free_request)
                iframeHtml = '<iframe class="col-12" src="https://maps.google.com/maps?q=' + data.lat + ', ' + data.lng + '&z=15&output=embed" width="320" height="330" frameborder="0" style="border:0;padding:0px;" allowfullscreen></iframe>'
                $("#map-article").empty();
                $('#map-article').append(iframeHtml)
                // add to near cities
                $('.near_city_tab1').text(data.near_cities.city1)
                $('#near_city1').text(data.near_cities.city1)
                $('#near_country1').text(data.near_cities.country1)
                $('#near_distance1').text(data.near_cities.distance1)
                $(".tab1").attr("lat",data.near_cities.lat1);
                $(".tab1").attr("lng",data.near_cities.lng1);

                $('.near_city_tab2').text(data.near_cities.city2)
                $('#near_city2').text(data.near_cities.city2)
                $('#near_country2').text(data.near_cities.country2)
                $('#near_distance2').text(data.near_cities.distance2)
                $(".tab2").attr("lat",data.near_cities.lat2);
                $(".tab2").attr("lng",data.near_cities.lng2);

                $('.near_city_tab3').text(data.near_cities.city3)
                $('#near_city3').text(data.near_cities.city3)
                $('#near_country3').text(data.near_cities.country3)
                $('#near_distance3').text(data.near_cities.distance3)
                $(".tab3").attr("lat",data.near_cities.lat3);
                $(".tab3").attr("lng",data.near_cities.lng3);
                $('.near_cities_container').show()
            },
        })
    }
})
