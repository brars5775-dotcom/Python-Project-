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
def document_detail(request, id):
    try:
        document = Document.objects.get(id=id)

        data = {
            "id": document.id,
            "name": document.name,
            "status": document.status,
            "uploaded_at": document.uploaded_at,
            "extraction_timestamp": document.extraction_timestamp
        }

        return JsonResponse(data)

    except Document.DoesNotExist:
        return JsonResponse({"error": "Document not found"}, status=404)