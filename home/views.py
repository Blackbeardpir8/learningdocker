from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    return JsonResponse({
        "status" : 200,
        "message" : "running from docker"
    })