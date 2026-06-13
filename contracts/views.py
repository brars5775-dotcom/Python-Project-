from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Document
from .serializers import DocumentSerializer
from .services import parse_contract


def home(request):
    return JsonResponse({
        "message": "Contract Parsing API is running"
    })

@api_view(["GET", "POST"])
def upload_contract(request):

    if request.method == "GET":
        return Response({
            "message": "Upload a file using POST."
        })

    uploaded_file = request.FILES.get("file")

    if not uploaded_file:
        return Response(
            {"error": "No file uploaded"},
            status=400
        )

    document = Document.objects.create(
        file=uploaded_file,
        filename=uploaded_file.name
    )

    uploaded_file.seek(0)

    text = uploaded_file.read().decode(
        "utf-8",
        errors="ignore"
    )

    print("TEXT:", text)

    parse_contract(document, text)

    serializer = DocumentSerializer(document)

    return Response(serializer.data)