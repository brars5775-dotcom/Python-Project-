from django.urls import path
from .views import (
     home,
     upload_contract,
     list_documents,
     view_clauses,
     view_risks
) 

urlpatterns = [
    path("", home),
    path("upload/", upload_contract),
    path("documents/", list_documents),
    path(
        "clauses/<int:document_id>/",
        view_clauses
    ),
    path(
        "risks/<int:document_id>/",
        view_risks
    ),
]