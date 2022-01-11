#! usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/12/28 16:24
# @Author: wangjunjie
# @File: forms.py
# @Des:

from django import forms
from .models import ArticlePost


# 写文章的表单类
class ArticlePostForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = ArticlePost
        # 定义表单包含的字段
        fields = ('title', 'body', 'tags', 'avatar')
