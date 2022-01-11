#! usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2022/1/4 10:58
# @Author: wangjunjie
# @File: forms.py
# @Des:

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']