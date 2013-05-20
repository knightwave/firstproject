from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from website.blog.models import *

import json

def post(request):
	errors = []
	success = []
	messages = []
	posts = Post.objects.all()
	comments = Comment.objects.all()
	if request.method == "POST":
		title_null = post_null = 0
		post = request.POST['post']
		title = request.POST['post_title']
		if title == "":
			title_null = 1
			errors.append("Title cannot be empty.")
		if post == "":
			post_null = 1
			errors.append("Post cannot be empty.")
		if title_null == 0 and post_null == 0:	
			try:
				post_object = Post.objects.get(title=title, author=Muon.objects.get(user=request.user))
				errors.append("There is already a post by the same title posted by you. Please choose a different title or edit the previous post.")
			except:
				post_object = Post.objects.create(title=title,author= Muon.objects.get(user=request.user), content=post)		
				post_object.save()
			return render_to_response("blog/blog.html",{'errors':errors,'success':success,'posts':posts,'comments':comments},context_instance=RequestContext(request))	
	else:
		return render_to_response("blog/blog.html",{'errors':errors,'success':success,'posts':posts,'comments':comments},context_instance=RequestContext(request))	

def comment(request):
	if request.is_ajax() and request.method=="POST":
		post_id = request.POST['post_id']
		post_content = request.POST['post_comment']
		c = Comment.objects.create(post_id = post_id, author=Muon.objects.get(user=request.user),content=post_content)
		c.save()
		return HttpResponseRedirect("/blog/post/")
	else:
		return HttpResponse("Wrong Page Buddy ;(")
