from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status

from django.http import JsonResponse
from .serializers import DocumentSerializer
from .tasks import task1, task2, task3

import os
from metabolite.settings import MEDIA_ROOT, BASE_DIR, MEDIA_URL

class UploadDocumentView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = DocumentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FilterMetabolitesView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        document = request.data["document"]
        file_path = os.path.normcase(BASE_DIR)+os.path.normcase(document)
        pc, lpc, plasmalogen = task1(file_path)
        pcfile_path = os.path.normcase(MEDIA_ROOT)+os.path.normcase('\output\output_pc.xlsx')
        lpcfile_path = os.path.normcase(MEDIA_ROOT)+os.path.normcase('\output\output_lpc.xlsx')
        plasmalogenfile_path = os.path.normcase(MEDIA_ROOT)+os.path.normcase('\output\output_plasmalogen.xlsx')
        pc.to_excel(pcfile_path)
        lpc.to_excel(lpcfile_path)
        plasmalogen.to_excel(plasmalogenfile_path)

        data = {'file_path':[
            (os.path.normcase(MEDIA_URL)+os.path.normcase('\output\output_pc.xlsx'), 'Extract metabolite ids ending with: PC'),
            (os.path.normcase(MEDIA_URL)+os.path.normcase('\output\output_lpc.xlsx'), 'Extract metabolite ids ending with: LPC'),
            (os.path.normcase(MEDIA_URL)+os.path.normcase('\output\output_plasmalogen.xlsx'), 'Extract metabolite ids ending with: plasmalogen')]
            }
        return JsonResponse(data, status=status.HTTP_201_CREATED)

class RoundOffRetentionView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        document = request.data["document"]
        file_path = os.path.normcase(BASE_DIR)+os.path.normcase(document)
        df = task2(file_path)
        dffile_path = os.path.normcase(MEDIA_ROOT)+os.path.normcase('\output\output_roundoff.xlsx')
        df.to_excel(dffile_path)
        data = {
            'file_path':[
            (os.path.normcase(MEDIA_URL)+os.path.normcase('\output\output_roundoff.xlsx'), 
            'Add a new column “Retention Time Roundoff (in mins)"')]
            }

        return JsonResponse(data, status=status.HTTP_201_CREATED)

class MeanRetentionView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        document = request.data["document"]
        file_path = os.path.normcase(BASE_DIR)+os.path.normcase(document)
        df = task3(file_path)
        dffile_path = os.path.normcase(MEDIA_ROOT)+os.path.normcase('\output\output_meanretention.xlsx')
        df.to_excel(dffile_path)
        data = {
            'file_path':[
            (os.path.normcase(MEDIA_URL)+os.path.normcase('\output\output_meanretention.xlsx'), 
            'Mean of all the metabolites which have same "Retention Time Roundoff"')]
            }
        return JsonResponse(data, status=status.HTTP_201_CREATED)