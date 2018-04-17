# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_page
import json
import os


def index(request):
    return HttpResponse(u"welcome to nws !~~~")

def searchdb(request):
    # 读取数据库等 并渲染到网页
    # 数据库获取的结果保存到 queryset 中
    queryset=''
    return render(request, 'index.html', {'queryset':queryset})

    # Create your views here.


@cache_page(60 * 15) # 秒数，这里指缓存 15 分钟，不直接写900是为了提高可读性
def cachepage(request):
    # 读取数据库等 并渲染到网页
    queryset=''
    return render(request, 'index.html', {'queryset':queryset})

#generate static html page 
    '''
def my_view(request):
    context = {'some_key': 'some_value'}
 
    static_html = '/path/to/static.html'
 
    if not os.path.exists(static_html):
        content = render_to_string('template.html', context)
        with open(static_html, 'w') as static_file:
            static_file.write(content)
 
    return render(request, static_html)

def login(request):
    m = Member.objects.get(username=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['member_id'] = m.id
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Your username and password didn't match.")
         
     '''    
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

    

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

def home(request):
    List = ['自强学堂', '渲染Json到模板']
    Dict = {'site': '自强学堂', 'author': '涂伟忠'}
    return render(request, 'home2.html', {
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })

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

