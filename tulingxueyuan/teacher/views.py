from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def do_normalmap(request):
    return HttpResponse("This is normalmap")


def withparam(request,year,month):
    return HttpResponse("This is with param {0} , {1}".format(year , month))