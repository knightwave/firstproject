# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext 
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User

from models import *

def loginRequest(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/muon/home')
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None and user.is_active:
			login(request,user)
			return HttpResponseRedirect("/muon/home/")	
	return render_to_response("muon/login.html",{},context_instance=RequestContext(request))

def register(request):
	if request.method == "POST":
		errors=[]
		success=[]
		if request.method=="POST":
			username=request.POST['username']
			name=request.POST['name']
			password1 = request.POST['password1']
			password2 = request.POST['password2']	
			if password1 != password2:
				errors.append("The entered passwords donot match. Please enter again.")
				return render_to_response("muon/register.html",{'errors':errors, 'success':success},context_instance=RequestContext(request))
			try:
				user=User.objects.get(username=username)
				errors.append('Username '+username+ ' already exists. Choose another username.')
				return render_to_response("muon/register.html",{'errors':errors,'success':success},context_instance=RequestContext(request))
			except:
				user=User.objects.create(username=username)
				user.set_password(password1)
				user.save()
				muon=Muon.objects.create(user=user)
				muon.save()
				success.append('User '+username+' created successfully!')
				return render_to_response("muon/register.html",{'errors':errors,'success':success},context_instance=RequestContext(request))
	else:
		return render_to_response('muon/register.html',{},context_instance=RequestContext(request))

def home(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/muon/login/')
	print request.user.username
	if request.user.username=="knightwave":
		request.session['flag_admin']=1
		flag_admin=1
	else:
		request.session['flag_admin']=0
		flag_admin=0
	username=request.user.username
	return render_to_response("muon/home.html",{'username':username,'flag_admin':flag_admin,'blog':1},context_instance=RequestContext(request))
	
def addUser(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/muon/login')
	errors=[]
	success=[]
	if request.method=="POST":
		username=request.POST['username']
		name=request.POST['name']
		try:
			user=User.objects.get(username=username)
			errors.append('Error while creating the user. Username '+username+ ' already exists. Choose another username.')
			return render_to_response("muon/addUser.html",{'errors':errors,'success':success},context_instance=RequestContext(request))
		except:
			user=User.objects.create(username=username)
			user.set_password('hello')
			user.save()
			muon=Muon.objects.create(user=user)
			muon.save()
			success.append('User '+username+' created successfully!')
			return render_to_response("muon/addUser.html",{'errors':errors,'success':success},context_instance=RequestContext(request))
	else:
		return render_to_response('muon/addUser.html',{},context_instance=RequestContext(request))
		
def logoutRequest(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/muon/login')
	logout(request)
	return HttpResponseRedirect('/muon/login')

def listUsers(request):
	errors=[]
	success=[]
	messages=[]
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/muon/login')
	if request.user.username=="knightwave":
		request.session['flag_admin']=1
		flag_admin=1
	else:
		request.session['flag_admin']=0
		flag_admin=0
	users=[]
	users=User.objects.all()
	return render_to_response('muon/home.html',{'errors':errors,'messages':messages,'success':success,'users':users,'flag_admin':flag_admin},context_instance=RequestContext(request))

def deleteUser(request,username=None):
	success=[]
	errors=[]
	if request.method == "POST":
		username=request.POST['username']
		try:
			username=str(username)
			user=User.objects.get(username=username)
			muon_user = Muon.objects.get(user=user)
			muon_user.delete()
			user.delete()
			success.append('User '+username+' deleted successfully!')
			return render_to_response("muon/addUser.html",{'success':success},context_instance=RequestContext(request))
		except:
			error_flag=1
			errors.append("Error while deleting the user")
		return render_to_response("muon/addUser.html",{'success':success,'errors':errors},context_instance=RequestContext(request))
	else:
		errors.append('Error')	
		return render_to_response("muon/addUser.html",{'success':success,'errors':errors},context_instance=RequestContext(request))
