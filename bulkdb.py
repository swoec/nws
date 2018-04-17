#!/usr/bin/env python
#coding:utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nws.settings")


 
import django
if django.VERSION >= (1,7):
    django.setup()

 
def main():
    from nw.models import Blog
    f = open('history.txt')
    BlogList = []
    for line in f:
        title,content = line.split('****')
        blog = Blog(name=title,tagline=content)
        BlogList.append(blog)
    f.close()
     
    Blog.objects.bulk_create(BlogList)


def mains():
    from nw.models import Blog
    f = open('history.txt')
     
    BlogList = []
    for line in f:
        parts = line.split('****')
        BlogList.append(Blog(name=parts[0], tagline=parts[1]))
     
    f.close()
         
    # 以上四行 也可以用 列表解析 写成下面这样
    # BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]
     
    Blog.objects.bulk_create(BlogList)

 
if __name__ == "__main__":
    mains()
    print('Done!')
