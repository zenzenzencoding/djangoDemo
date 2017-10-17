#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/10/17 15:37
@Author  : wang.zheng@ctrip.com
@File    : forms.py
"""
from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()