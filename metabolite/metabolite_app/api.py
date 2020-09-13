from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from django.http import JsonResponse
from .serializers import UploadDocumentSerializer
from .tasks import task1, task2, task3

import os
from metabolite.settings import MEDIA_ROOT

class UploadDocumentView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = UploadDocumentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilterMetabolitesView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        file_path = os.path.join(MEDIA_ROOT, request.session["document"])

        print(file_path)
        
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoundOffRetentionView(APIView):
    permission_classes = [permissions.AllowAny]

class MeanRetentionView(APIView):
    permission_classes = [permissions.AllowAny]
