from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from website.blog.models import *
from django.utils import simplejson
from tagging.models import Tag, TaggedItem

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
		tags = request.POST['tags']
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
				post_object = Post.objects.create(title=title,author= Muon.objects.get(user=request.user), content=post, tags=tags)		
				post_object.save()
			return render_to_response("blog/blog.html",{'errors':errors,'success':success,'posts':posts,'comments':comments},context_instance=RequestContext(request))	
	else:
		return render_to_response("blog/blog.html",{'errors':errors,'success':success,'posts':posts,'comments':comments},context_instance=RequestContext(request))	

def comment(request):
	errors = []
	success = []
	messages = []
	if request.is_ajax() and request.method=="POST":
		post_id = request.POST['post_id']
		post_content = request.POST['post_comment']
		comment_author = Muon.objects.get(user=request.user) 
		c = Comment.objects.create(post_id = post_id, author=comment_author,content=post_content)
		c.save()
		data = {"success":1}
		data['post_id'] = post_id
		data['comment_author'] = str(comment_author)
		data['comment'] = post_content
		return HttpResponse(simplejson.dumps(data), content_type="application/json")
	else:
		return HttpResponse("Wrong Page Buddy ;(")

def tags(request, tag=None):
	success = []
	errors = []
	messages = []
	post_tags = Post.objects.filter(tags__contains=tag)
	print post_tags
	comments = []
	for post in post_tags:
		comments.append(Comment.objects.filter(post=post))
	return render_to_response("blog/tags.html",{'errors':errors,'success':success,'posts':post_tags,'comments':comments},context_instance=RequestContext(request))	
	
def with_tag(request, tag=None, object_id=None, page=1): 
	print 
	query_tag = Tag.objects.get(name=tag)
	entries = TaggedItem.objects.get_by_model(Post, query_tag)
	entries = entries.order_by('-date') 
	return render_to_response("blog/with_tag.html",{'tag':tag, 'entries':entries},context_instance=RequestContext(request))  	
