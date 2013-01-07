from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render_to_response, render
import time

def calc(request):
    t1 = time.time()
    for i in range(100000):
        a = 'a'*100
        b = 'b'*100
        c = a+b
    t2 = (time.time() - t1) * 1000

    return HttpResponse('hello world from django: %s ms'%t2)

def trender(request):
    num = range(1000)
    return render_to_response('loop_t.html', {'num':num})

def empty_template(request):
    return render_to_response('plain.html', {})

def bigrender(request):
    return render_to_response('big_render.html', {})
