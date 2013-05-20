$(document).ready(function () {
	var input = document.getElementById("id_file"), 
		formdata = false;

	function showUploadedItem (source) {
  		var list = document.getElementById("image-list"),
	  		li   = document.createElement("li"),
	  		img  = document.createElement("img");
  		img.src = source;
  		li.appendChild(img);
		list.appendChild(li);
	}   

	if (window.FormData) {
  		formdata = new FormData();
  		document.getElementById("btn").style.display = "none";
	}
	
 	input.addEventListener("change", function (evt) {
 		document.getElementById("response").innerHTML = "<img src='{{ STATIC_URL }}images/ajax-loader.gif' height='100px' width='100px' />"
 		var i = 0, len = this.files.length, img, reader, file;
	
		for ( ; i < len; i++ ) {
			file = this.files[i];
	
			if (true) {
				if ( window.FileReader ) {
					reader = new FileReader();
					reader.onloadend = function (e) { 
						showUploadedItem(e.target.result, file.fileName);
					};
					reader.readAsDataURL(file);
				}
				if (formdata) {
					formdata.append("file", file);
				}
			}	
		}
	
		if (formdata) {
			formdata.append('csrfmiddlewaretoken',$('input[name=csrfmiddlewaretoken]').val());
			$.ajax({
				url: '/ebooks/list/',
				type: 'post',
				data: formdata,
				processData: false,
				contentType: false,
				error : function (jqXHR, textStatus, errorThrown) {
					console.log(textStatus, errorThrown);	
				},
				success: function (res) {
					document.getElementById("response").innerHTML = res; 
				}
			});
		}
	}, false);
});
