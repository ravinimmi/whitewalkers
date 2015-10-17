$(document).ready(function(){
	$('a.ajax-link').click(function(e){
		e.preventDefault();
		$('.mdl-layout__tab.is-active').removeClass('is-active');
		$(e.currentTarget).addClass('is-active');
		container = $(this).data('container')
		$.get($(this).attr('href'), function(data){
			$(container).html(data)
		})
		.fail(function(){
			$(container).html('<h3>Ooops!!</h3>')
		})
	});
	$('#create-survey').find('a.ajax-link.is-active').trigger('click');
});