var map = null;
var markers = [];

function init_map() {
    map = new google.maps.Map(document.getElementById('map-canvas'));
    var mapOptions = {
      center: { lat: 37.4253498, lng: -122.0765002},
      zoom: 8
    };
}

function get_messages(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    $.get("/search?lat="+lat+"&lng="+lng,
        function(messages) {
            for(var m_i; m_i < messages.length; m_i++){
                var m = messages[m_i]
                var marker = new google.maps.Marker({
                    position: new google.maps.LatLng(m.lat, m.lng),
                    map: map,
                    icon: m.img_url
                });
                markers.push(marker);
            }
        }
    );
}

function start_messages() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(get_messages);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

// google.maps.event.addDomListener(window, 'load', init_map);
// console.log("HEllO");
