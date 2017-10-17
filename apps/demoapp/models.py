#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/10/13 16:21
@Author  : wang.zheng@ctrip.com
@File    : 
"""
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def my_property(self):
        return u"作者:"+self.name

    my_property.short_description = "name of the person"
    description = property(my_property)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):  # __str__ on Python 3
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name="邮箱")

    def __str__(self):  # __str__ on Python 3
        return self.name

class Article(models.Model):
    title = models.CharField(u'标题',max_length=256)
    content = models.TextField(u'内容',default="")
    pub_date = models.DateTimeField(u'发布时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u"更新时间",auto_now=True,null=True)

    def __str__(self):
        return self.title



class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(u'发布时间',auto_now_add=True,editable=True)
    mod_date = models.DateField(u'修改时间',auto_now=True,null=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):  # __str__ on Python 3
        return self.headline