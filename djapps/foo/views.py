from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response, render

def home(request):
    return HttpResponse('hello world from django')

def uset(request):
    num = range(1000)
    return render_to_response('loop_t.html', {'num':num})