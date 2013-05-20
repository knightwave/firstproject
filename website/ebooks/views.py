from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from models import Document
from forms import UploadForm
from website.settings import MEDIA_ROOT, PROJECT_ROOT
from website.ebooks.constants import list_problems

import filecmp
import os
import subprocess
import threading
threading._DummyThread._Thread__stop = lambda x: 42
def list(request):
	if request.is_ajax():
		print "ajax entered"
		print request.FILES
		form = UploadForm(request.POST,request.FILES)
		if form.is_valid():
			print 'form validated'
			files = request.FILES.getlist('file')
			for file in files:
				path = MEDIA_ROOT+'ebooks/'+str(file)
				destination = open(path, 'wb+')
				for chunk in file.chunks():
					destination.write(chunk)
				destination.close()
			for file in files:
				path = MEDIA_ROOT+'ebooks/'+str(file)
				destination = open(path, 'wb+')
				a = destination.read()
				print a
				destination.close()
		return HttpResponse('done \m/');

	output = []
	error = []
	rlt = None
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			file = Document(file = request.FILES['file'])
			file.save()
			files = request.FILES.getlist('file')
			for file in files:
				path = MEDIA_ROOT+'ebooks/'+str(file)
				destination = open(path, 'wb+')
				for chunk in file.chunks():
					destination.write(chunk)
				destination.close()
			for file in files:
				path = MEDIA_ROOT+'ebooks/'+str(file)
				destination = open(path, 'r')
				a = destination.read()
				destination.close()
			for file in files:
				path = MEDIA_ROOT+'ebooks/'+str(file)
				a=b=''
				p = subprocess.Popen(['g++',path])
				#a,b = p.communicate()
				p.wait()
				print a
				print 'goo boy'
				a = os.linesep.join([s for s in a.splitlines() if s])
				b = os.linesep.join([s for s in b.splitlines() if s])
				output.append(a)
				error.append(b)
				if not b: 
					pr = subprocess.call(['./a.out'])
					file = open('output.txt','r')
					print file.read()
					file.close()
					file = open('1.txt','r')
					print file.read()
					file.close()	
					rlt = filecmp.cmp('output.txt','1.txt',shallow=False)
					print 'pramod'	
					print rlt
			"""
			import subprocess  

			basename = "CodeGenTest";  
			execname = basename;  
			srcname = basename + ".cpp";  

			codeList = [];
			codeList.append("#include<iostream>")
			codeList.append("#include <stdio.h>");  
			codeList.append("using namespace std;int main(int argc, char *argv[])\n{");  
			codeList.append("printf(\"Hello world.\\n\");");  
			codeList.append("int a;cin>>a;");  
			codeList.append("}");  

			# Convert codelist to string.  
			codeList.append("");  
			codeString = "\n".join(codeList);  
			
			# Print code to output source file  
			outfile=open(srcname,'w');  
			outfile.write(codeString);  
			outfile.close();
			
			print "Compile.";  
			cmd = ["g++", srcname, "-o", execname];  
			p = subprocess.Popen(cmd);  
			p.wait();  
			
			subprocess.call(["./"+execname,'<','input.txt','>','output.txt']);
			"""
	else:
		form = UploadForm()
	dir_path = os.path.join(MEDIA_ROOT,'ebooks/')
	files = []
	for file in os.listdir(dir_path):
		files.append(os.path.join(file))
	return render_to_response('ebooks/list.html', {'files':tuple(files), 'error':error, 'output':output, 'form':form}, context_instance = RequestContext(request))

def compile(request):
	if request.method == "POST":
		print request.POST
		code = request.POST['code']
		input = request.POST['input']
		codefile_path = PROJECT_ROOT + '/media/problems/code_file.cpp'
		code_file = open(codefile_path,'w')
		code_file.write(code)
		code_file.close()		
		inputfile_path = PROJECT_ROOT + '/media/problems/input_file.txt' 
		input_file = open(inputfile_path,'w')
		input_file.write(input)
		input_file.close()
		compile = subprocess.Popen(["g++",codefile_path,"-w","-o","./a.out"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		compile_output, compile_error = compile.communicate() 
		error=0
		read_out = ''
		if compile_error:
			error = 1
		else:
			result = subprocess.Popen(["./a.out"], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=False)
			out,err = result.communicate(input=input)
			for line in out:
				read_out = read_out+line
		return render_to_response("ebooks/compiler.html",{'result':True,'code_value':code,'input_value':input,'output':read_out,'error':error,'compile_error':compile_error},context_instance=RequestContext(request))
	else:
		return render_to_response("ebooks/compiler.html",{'code_value':"",'input_value':""},context_instance=RequestContext(request))

def problems(request, problem):
	if problem not in zip(*list_problems)[0]:
		return HttpResponse("Wrong page :(")
	problem_path = PROJECT_ROOT + '/media/problems/'+problem+'/question.txt' 
	error=0
	statement = ""
	try:
		file = open(problem_path,"r")
		for line in file.read():
			statement+= line
		file.close()
	except:
		error=1
	dict_problems = dict(list_problems)
	problem_key = problem
	problem_value = dict_problems[problem]
	return render_to_response("ebooks/problems.html",{'problemKey':problem_key,'problemValue':problem_value,'list_problems':list_problems,'statement':statement},context_instance=RequestContext(request))

def submit(request, problem):
	if request.method == "POST":
		code = request.POST['code']
		codefile_path = PROJECT_ROOT + '/media/problems/code_submit.cpp'
		code_file = open(codefile_path, 'w')
		code_file.write(code)
		code_file.close()
		inputfile_path = PROJECT_ROOT + '/media/problems/'+problem+'input.txt' 
		input_file = open(inputfile_path,'w')
		input_file.write(input)
		input_file.close()
		compile = subprocess.Popen(["g++",codefile_path,"-w","-o","./a.out"],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		compile_output, compile_error = compile.communicate() 
		error=0
		read_out = ''
		if compile_error:
			error = 1
		else:
			result = subprocess.call("./a.out < input_file.txt > output.txt", shell=True)
			#kill a thread after timeout
			out = open('output.txt','r')
			for line in out:
				read_out = read_out+line
			out.close()
	else:
		return render_render_response()
