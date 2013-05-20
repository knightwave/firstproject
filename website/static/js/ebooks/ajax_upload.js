$(document).ready(function(){
	$('button').click(function(){
		var formData = new FormData($('form[name=change]')[0]);;
		var data  =  $('form').serialize();
		$.ajax({
			url:'/ebooks/list/',
			type: 'post',
			data: formData,
			success: function(data){						
				alert(data);	
			},
			processData: false,
			contentType: false
		});
		return false;	
	});
	
});
