$(document).ready(function() {
	$('.clickme').click(function() {
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
	// console.log(data)
	m = JSON.parse(data)
	// console.log(m['id'])
	$('#'+"td"+m.id).html("<td><p>"+m.title+"</p><p><a href="+m.url+">Click to go!</a></p><p>"+m.doc+"</p></td>");
}