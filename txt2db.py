#!/usr/bin/env python
#coding:utf-8
 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nws.settings")
 
'''
Django 版本大于等于1.7的时候，需要加上下面两句
import django
django.setup()
否则会抛出错误 django.core.exceptions.AppRegistryNotReady: Models aren't loaded yet.
'''
 
import django
if django.VERSION >= (1, 7):#自动判断版本
    django.setup()
 
 
def main():
    from nw.models import Blog
    f = open('history.txt')
    for line in f:
        title,tagline = line.split('****')
        Blog.objects.create(name=title,tagline=tagline)
    f.close()
 
if __name__ == "__main__":
    main()
    print('Done!')# -*- coding: utf-8 -*-

