#! usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/12/29 15:34
# @Author: wangjunjie
# @File: forms.py
# @Des: 账户密码表单类

from django import forms
from django.contrib.auth.models import User
from .models import Profile


# 登录表单，继承了forms.Form类
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


# 注册用户表单
class UserRegisterForm(forms.ModelForm):
    # 复写User的密码
    password = forms.CharField()
    password2 = forms.CharField()
    #覆写某字段之后，内部类class Meta中的定义对这个字段就没有效果了，
    # 所以fields不用包含password。
    class Meta:
        model = User
        fields = ('username', 'email')

    # 对两次输入的密码是否一致进行检查
    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致，请重试。")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')