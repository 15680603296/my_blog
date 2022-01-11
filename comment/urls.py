#! usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/1/4 10:45
# @Author: wangjunjie
# @File: urls.py
# @Des:

from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    # 发表评论
    path('post-comment/<int:article_id>/', views.post_comment, name='post_comment'),
]