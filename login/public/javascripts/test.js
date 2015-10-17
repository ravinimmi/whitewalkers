$(document).ready(function(){
	$('#age-range').change(function(){
	 if($(this).is(':checked')){
	 	$(this).parent().append('<input type="text" id="from" placeholder="from"><input type="text" id="to" placeholder="to">');
	 }
	});

	$('#users-fixed').change(function(){
	 if($(this).is(':checked')){
	 	$(this).parent().append('<input type="text" id="num_users" placeholder="Number of Usrs">');
	 }
	});

	$("#done").click(function(){
		var male = $("#male").is(':checked');
		var female = $("#female").is(':checked');
		var unlimited_age = $("#age-any").is(':checked');
		var age_from = $("#from").val();
		var age_to = $("#to").val();
		var unlimited_users = $("#unlimited-users").is(':checked');
		var num_users = $("#num_users").val();
		var applyall = $("#aplly-all").is(':checked');
		console.log(male+" "+female+" "+unlimited_age+" "+age_from+" "+age_to+" "+unlimited_users+" "+num_users+" "+aspplyall);
	});
});