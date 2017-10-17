#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/10/13 16:21
@Author  : wang.zheng@ctrip.com
@File    : 
"""
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddForm
def index(request):
    #return HttpResponse(u"欢迎光临umi学院")
    if request.method=="POST":
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a)+int(b)))
    else:
        form = AddForm()
    return render(request, 'index.html', {'form':form})

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    return HttpResponse(int(a)+int(b))