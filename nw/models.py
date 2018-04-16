# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

 
 
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    def __str__(self):
    # 在Python3中使用 def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
 
    def __str__(self):  # __str__ on Python 3
        return self.name
   
    
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=50)
    qq = models.CharField(max_length=10)
    addr = models.TextField()
    email = models.EmailField()
 
    def __str__(self):
        return self.name
    
 
class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()
 
    def __str__(self):  # __str__ on Python 3
        return self.headline
 
 
 
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()  # 文章的打分
    tags = models.ManyToManyField('Tag')
 
    def __str__(self):
        return self.title
 
 
@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)
 
    def __str__(self):
        return self.name