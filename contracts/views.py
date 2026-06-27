from django.http import JsonResponse
from .models import Document
from django.shortcuts import render
def home(request):
    return JsonResponse({
        "message": "Contract Parsing API is running"
    })

def document_list(request):
    documents = Document.objects.all()

    data = []

    for doc in documents:
        data.append({
            "id": doc.id,
            "name": doc.name,
            "status": doc.status,
            "uploaded_at": doc.uploaded_at
        })

    return JsonResponse(data, safe=False)