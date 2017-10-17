# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2017/10/13 16:21
@Author  : wang.zheng@ctrip.com
@File    : 
"""
from django.contrib import admin

# Register your models here.

from apps.demoapp.models import Article,Author,Blog,Entry,Person

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time')
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name","age","description")

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)
        try:
            search_term_as_int = int(search_term)
            queryset |= self.model.objects.filter(age=search_term_as_int)
        except:
            pass
        return queryset, use_distinct

admin.site.register(Article,ArticleAdmin)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Entry)
admin.site.register(Person,PersonAdmin)

