from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Document,
    ExtractedClause,
    RiskFlag
)

from .serializers import (
    DocumentSerializer,
    ExtractedClauseSerializer,
    RiskFlagSerializer
)

from .services import parse_contract

import os
import logging

logger = logging.getLogger(__name__)


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

    try:

        uploaded_file = request.FILES.get("file")

        if not uploaded_file:
            return Response(
                {"error": "No file uploaded"},
                status=400
            )

        ALLOWED_EXTENSIONS = [".pdf", ".docx", ".txt"]

        extension = os.path.splitext(
            uploaded_file.name
        )[1].lower()

        if extension not in ALLOWED_EXTENSIONS:
            return Response(
                {
                    "error": "Only PDF, DOCX and TXT files are allowed."
                },
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

        return Response({
            "message": "File uploaded successfully",
            "document_id": document.id,
            "filename": document.filename,
            "data": serializer.data
        })

<<<<<<< HEAD
        except Exception as e:

        logger.error(
            f"Upload Error: {str(e)}",
            exc_info=True
        )

        return Response(
            {
                "error": "Something went wrong while processing the file."
            },
            status=500
        )


@api_view(["GET"])
def list_documents(request):

    documents = Document.objects.all()

    serializer = DocumentSerializer(
        documents,
        many=True
    )

    return Response(serializer.data)


@api_view(["GET"])
def view_clauses(request, document_id):

    clauses = ExtractedClause.objects.filter(
        document_id=document_id
    )

    serializer = ExtractedClauseSerializer(
        clauses,
        many=True
    )

    return Response(serializer.data)


@api_view(["GET"])
def view_risks(request, document_id):

    risks = RiskFlag.objects.filter(
        document_id=document_id
    )

    serializer = RiskFlagSerializer(
        risks,
        many=True
    )

    return Response(serializer.data)
    
>>>>>>> fc02632 (Added document, clause and risk listing APIs)
