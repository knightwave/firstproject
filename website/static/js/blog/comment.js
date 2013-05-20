$(document).ready(function(){
	$('input[name=comment_submit]').click(function(){
		//	var formData = new FormData($('form[name=change]')[0]);;
		var form = $(this).closest('form');
		var formData  =  $(form).serialize();
		alert(formData['post_comment']);
		$.ajax({
			url:'/blog/comment/',
			type: 'post',
			data: formData,
			success: function(data){						
				alert(data);	
			},
			//processData: false,
			//contentType: false
		});
		return false;	
	});	
});
