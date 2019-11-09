from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    """
    首页访问
    :return:
    """
    return HttpResponse("perfect")