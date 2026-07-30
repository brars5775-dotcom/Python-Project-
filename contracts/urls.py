from django.urls import path
from .views import (
    home,
    upload_contract,
    list_documents,
    document_detail,
    delete_document,
    view_clauses,
    view_risks,
)

urlpatterns = [
    path("", home),

    path("upload/", upload_contract),

    path("documents/", list_documents),

    path(
        "documents/<int:document_id>/",
        document_detail
    ),

    path(
        "documents/delete/<int:document_id>/",
        delete_document
    ),

    path(
        "clauses/<int:document_id>/",
        view_clauses
    ),

    path(
        "risks/<int:document_id>/",
        view_risks
    ),
]