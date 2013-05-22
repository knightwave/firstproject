$(document).ready(function(){
	$('input[name=comment_submit]').click(function(){
		
		var form = $(this).closest('form');
		var formData  =  $(form).serialize();
		if($(form).find('textarea[name=post_comment]').val() == ''){
			return false;	
		}
		//alert(formData['post_comment']);
		$.ajax({
			url:'/blog/comment/',
			type: 'post',
			data: formData,
			dataType:"json",
			success: function(data){
				$('.comments_'+data['post_id']).append("<p style='background-color:lightblue;'>"+data['comment_author']+": "+data['comment']+"</p>");
				$(form).find('textarea[name=post_comment]').val('');
			},
		});
		return false;	
	});	
});
