from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from django.http import JsonResponse
from .serializers import UploadDocumentSerializer


class UploadDocumentView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = UploadDocumentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)