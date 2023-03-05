from django.urls import path
from .views import CowDiseaseDetection

urlpatterns = [
    path('cow-disease-detector', CowDiseaseDetection.as_view())
]
