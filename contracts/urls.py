from django.urls import path
from .views import home,document_list

urlpatterns = [
    path('', home),
    path('documents/',document_list),
]
