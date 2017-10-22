from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('Hello. This is temporary view.')
