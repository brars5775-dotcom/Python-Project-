from django.urls import path
from .views import home, upload_contract

urlpatterns = [
    path('', home),
    path('upload/', upload_contract),
]