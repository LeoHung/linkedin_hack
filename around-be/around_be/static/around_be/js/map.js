var map = null;
var markers = [];
var self = null;

var self_lat = null;
var self_lng = null;

function initialize(position) {
  map = new google.maps.Map(document.getElementById('map-canvas'), {
    zoom: 14,
    center: {lat: position.coords.latitude, lng:position.coords.longitude}
    // center: {lat: 37.4247649, lng: -122.0781952}
  });

  get_messages(position);
}

function start_initialize() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(initialize);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

// google.maps.event.addDomListener(window, 'load', initialize);
google.maps.event.addDomListener(window, 'load', start_initialize);

function get_messages(position) {
    var lat = position.coords.latitude;
    var lng = position.coords.longitude;
    $.get("/search?lat="+lat+"&lng="+lng,
        function(messages) {
            for(var m_i=0; m_i < messages.length; m_i++){
                var m = messages[m_i]
                var marker = new google.maps.Marker({
                    position: new google.maps.LatLng(m.lat, m.lng),
                    map: map,
                    animation: google.maps.Animation.DROP,
                    icon: {url:m.img_url, scaledSize: new google.maps.Size(30, 30)}
                });
                markers.push(marker);
            }
            console.log(markers);
        }
    );

    self = new google.maps.Marker({
        icon: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
        position : new google.maps.LatLng(lat, lng),
        map : map,
        animation: google.maps.Animation.BOUNCE
    });
}

// function start_messages() {
//     if (navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(get_messages);
//     } else {
//         x.innerHTML = "Geolocation is not supported by this browser.";
//     }
// }
