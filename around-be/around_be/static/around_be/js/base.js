$(document).ready(function() {
	$('#spots').click(function(event) {
		event.preventDefault();
		$.ajax({
			type: "GET",
			url: "/message/"+$(this).attr('id'),
			data: {
				
			},
			success: searchSuccess,
			dataType: 'html'
		});
	});
});

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}


function showPosition(position) {
    console.log("Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude);
}
