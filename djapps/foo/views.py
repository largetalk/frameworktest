from django.http import HttpResponse
from django.template import Template, Context

def home(request):
    return HttpResponse('hello world from django')
