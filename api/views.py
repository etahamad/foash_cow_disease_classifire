from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.files.storage import default_storage
from .predictors import CowDiseaseDetector


# Create your views here.
class CowDiseaseDetection(APIView):
    def post(self, request):
        file_uploaded = request.FILES.get('image')
        file_name = default_storage.save(file_uploaded.name, file_uploaded)
        file_url = default_storage.url(file_name)
        detector = CowDiseaseDetector()
        accuracy, prediction = detector.predict(file_url[1:])
        data = {
            'prediction': prediction,
            'accuracy': accuracy
        }
        return Response(data, status=200)
