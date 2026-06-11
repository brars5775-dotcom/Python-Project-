from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Contract Parsing API is running"
    })from django.shortcuts import render

# Create your views here.
