# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect



def index(request):
    return HttpResponse(u"welcome to nws !~~~")

# Create your views here.
    

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def indexs1(request):
    return render(request, 'home.html')

def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )
    
#def home(request):
 #   return render(request, 'ahome.html')

def home1(request):
    print("~~~~~~~~~~~~~~~~~~~~")
    string = u"Django，用它来建网站"
    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    List = map(str, range(10))# 一个长度为100的 List
    return render(request, 'ahome.html', {'string': string,'TutorialList': TutorialList,'info_dict': info_dict,'List': List})

def indexsum(request):
    return render(request, 'sum.html')
     
def summ(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    return HttpResponse(str(a+b))

