from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from website.blog.models import *
from django.core.mail import send_mail


def sendMail(request):
	if request.method == "POST":
		to_name = request.POST['to_name']
		from_name = request.POST['from_name']
		message = request.POST['message']
		send_mail('Subject', 'Hello World', 'pramod231193@gmail.com', ['theknightwave@gmail.com'], fail_silently=False)
		return render_to_response("mailserver/sendMail.html",{'Post':1},context_instance=RequestContext(request))	
	else:
		return render_to_response("mailserver/sendMail.html",{},context_instance=RequestContext(request))

