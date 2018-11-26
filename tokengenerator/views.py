# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import uuid

from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import Http404
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from tokengenerator.models import Tokenpool
from django.template.defaultfilters import slugify
import re
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import schedule
import time
from background_task import background
from threading import Timer







# def index(request):
# 	context = RequestContext(request)
	
# 	if request.method == 'POST' :
# 		return HttpResponse("gdgg");
# 	return render_to_response('shop/signup.html')
@csrf_exempt
def home(request):
	context = RequestContext(request)
	dataofsearch = []
	return render(request,"tokengenerator/home.html",{})
	

def tokengenerator(request):
	context = RequestContext(request)
	Timer(300, remove, ()).start()
	remove(schedule=300)
	dataofsearch = []
	token = uuid.uuid1()
	obj = Tokenpool(token = token)
	obj.save()
	return render(request,"tokengenerator/tokengenerator.html",{})
	


def seeall(request):
	context = RequestContext(request)
	alltoken = {}
	token = uuid.uuid1()
	user = Tokenpool.objects.filter()
	alltoken['alltoken'] = user
	return render(request,"tokengenerator/alltokens.html",alltoken)

def delete(request):
	context = RequestContext(request)
	if request.method == 'POST' :
		try:
			id=request.POST.get('id')
			Tokenpool.objects.filter(id=id).delete()
		except:
			pass
	return render(request,"tokengenerator/delete.html")


def assign(request):
	context = RequestContext(request)
	result={}
	try:
		obj=Tokenpool.objects.order_by('flag').first()
		obj.flag=1
		result['id']=obj.id
		result['token'] = obj.token
		obj.save()
		Timer(60, free(obj.id), ()).start()
	except Tokenpool.DoesNotExist:
		raise Http404
	return render(request,"tokengenerator/assign.html",result)

def unblock(request):
	context = RequestContext(request)
	if request.method == 'POST' :
		id=request.POST.get('id')
		try:
			obj=Tokenpool.objects.get(id=id)
			obj.flag=0
			obj.save()
		except:
			pass
	return render(request,"tokengenerator/unblock.html")

def claim(request):
	context = RequestContext(request)
	result={}
	if request.method == 'POST' :
		id=request.POST.get('id')
		try:
			obj=Tokenpool.objects.get(id=id)
			obj.flag=1
			result['token'] =obj.token
			result['id'] =obj.id
			obj.save()
		except:
			pass
	return render(request,"tokengenerator/reclaim.html",result)

@background(schedule=300)
def remove():
	time_threshold = datetime.now() - timedelta(minutes=5)
	results = Tokenpool.objects.filter(created_at__lt=time_threshold,alive=1)
	try:
		for ele in results:
			Tokenpool.objects.filter(id=ele.id).delete()
	except Tokenpool.DoesNotExist:
		pass
	return render(request,"tokengenerator/delete.html")


def alive(request):
	context = RequestContext(request)
	alltoken={}
	if request.method == 'POST' :
		id=request.POST.get('id')
		try:
			obj=Tokenpool.objects.get(id=id)
			obj.alive=0
			obj.save()

		except:
			pass
		user = Tokenpool.objects.filter()
		alltoken['alltoken'] = user
		
	return render(request,"tokengenerator/alltokens.html",alltoken)


def free(id):
	alltoken={}
	try:
		obj = Tokenpool.objects.get(id=id)
		obj.flag = 0
	except:
		pass
	user = Tokenpool.objects.filter()
	alltoken['alltoken'] = user
	return render(request,"tokengenerator/alltokens.html",alltoken)






	






# Create your views here.
