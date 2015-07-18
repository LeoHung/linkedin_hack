window.setInterval(function () {
    if (navigator.geolocation) {
    	console.log("succeed");
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        console.log("Geolocation is not supported by this browser.");
    }
}, 30000);

$(document).ready(function() {
	if (navigator.geolocation) {
    	console.log("succeed");
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        console.log("Geolocation is not supported by this browser.");
    }
});

function showPosition(position) {
	var id = $("#id").attr('name')
    $.ajax({
        url: "/search",
        type: "GET",
        data: {
        	lat: position.coords.latitude,
        	lng: position.coords.longitude
        },
        dataType : "json",
        success: function( items ) {
            $("#table").html("")
            $(items).each(function() {
            	$("#table").append(
            	"<tr id=\""+this.id+"\">"+
            	"<td style=\"width: 90px;\">"+
            	"<img src=\""+this.img_url+"\" height=\"30\" width=\"40\">"+
            	"</td>"+
            	"<td id=\"td"+this.id+"\"><a href=\"spot/"+this.id+"\">"+this.title+"</a></td>"+
                "<td><a>"+(parseFloat(this.dist)*300).toFixed(2)+"mi</a></td>"+
                "</tr>")
            });
        }
    });
}

$(document).ready(function() {
	$('.clickme').click(function(event) {
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

function searchSuccess(data, textStatus, jqXHR) {
	m = JSON.parse(data)
	$('#'+"td"+m.id).html("<td><p>"+m.title+"</p><p><a href="+m.url+">Click to go!</a></p><p>"+m.doc+"</p></td>");
}

