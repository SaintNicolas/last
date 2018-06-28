#from django.shortcuts import render
from django.http import HttpResponse
from fy import trans
# Create your views here.

def translate(request):  # 定义视图函数
    from_lang = request.GET['from_lang']  # 获取URL中的参数
    to_lang = request.GET['to_lang']  # 获取URL中的参数
    text = request.GET['words']  # 获取URL中的参数
    return HttpResponse(trans.trans(text, from_lang, to_lang))  # 返回响应内容对象

def translate2(request, words, from_lang, to_lang):  # 定义视图函数
    return HttpResponse(trans.trans(words, from_lang, to_lang))  # 返回响应内容对象