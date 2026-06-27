from django.http import JsonResponse
from django.shortcuts import render
def home(request):
    return JsonResponse({
        "message": "Contract Parsing API is running"
    })

# Create your views here.
