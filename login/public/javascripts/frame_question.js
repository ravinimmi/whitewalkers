$(document).ready(function(){
	$.get('/panel/templates', function(data){
		$('.right-side-container').html(data);
	})
});