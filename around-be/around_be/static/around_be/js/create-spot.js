$(document).ready(function() {
    if (navigator.geolocation) {
        console.log("succeed");
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        console.log("Geolocation is not supported by this browser.");
    }
});

function showPosition(position) {
    $("#lat").val(position.coords.latitude);
    $("#lng").val(position.coords.longitude)
}