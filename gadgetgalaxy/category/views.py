from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def category_list (request):
    return HttpResponse("<h1>category_list</h1>")

def category_new (request):
    return HttpResponse("<h1>category_new</h1>")

def category_update (request , id):
    return HttpResponse(f"<h1>category {id}</h1>")