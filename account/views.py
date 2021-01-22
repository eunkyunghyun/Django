from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse("Hello, World!")