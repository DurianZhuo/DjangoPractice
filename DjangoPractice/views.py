from django.http import HttpResponse
from django.shortcuts import render
from stuapp.models import *


def index_views(request):
    return HttpResponse('hello world')








