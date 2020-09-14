from rest_framework.views import APIView
from rest_framework import permissions, status

from django.http import JsonResponse
from .serializers import DocumentSerializer
from .tasks import task1, task2, task3
from .models import Document
from django.core.files.storage import default_storage
import os

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
        doc_id = request.data["doc_id"]
        document = Document.objects.get(pk=int(doc_id))
        document_path, _ = os.path.splitext(document.document.path)
        document_media_path, _ = os.path.splitext(str(document.document))
        
        # task1 function performs Operation1 on file and return 3 datasets 
        pc, lpc, plasmalogen = task1(document.document)
    
        # set output file path
        pcfile_path = document_path+'output_pc.xlsx'
        lpcfile_path = document_path+'output_lpc.xlsx'
        plasmalogenfile_path = document_path+'output_plasmalogen.xlsx'
        
        # save excel files
        pc.to_excel(pcfile_path)
        lpc.to_excel(lpcfile_path)
        plasmalogen.to_excel(plasmalogenfile_path)

        print(default_storage.url(document_media_path+'output_pc.xlsx'))
        data = {'file_path':[
            (default_storage.url(document_media_path+'output_pc.xlsx'), 'Extract metabolite ids ending with: PC'),
            (default_storage.url(document_media_path+'output_pc.xlsx'), 'Extract metabolite ids ending with: LPC'),
            (default_storage.url(document_media_path+'output_plasmalogen.xlsx'), 'Extract metabolite ids ending with: plasmalogen')
            ]}
        return JsonResponse(data, status=status.HTTP_201_CREATED)

class RoundOffRetentionView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        doc_id = request.data["doc_id"]
        document = Document.objects.get(pk=int(doc_id))
        document_path, _ = os.path.splitext(document.document.path)
        document_media_path, _ = os.path.splitext(str(document.document))
        
        # task2 function performs Operation2 on file and return  dataset
        df = task2(document.document)

        # save excel file
        dffile_path = document_path+'output_roundoff.xlsx'
        df.to_excel(dffile_path)

        data = {
            'file_path':[
            (default_storage.url(document_media_path+'output_roundoff.xlsx'), 
            'Add a new column “Retention Time Roundoff (in mins)"')]
            }

        return JsonResponse(data, status=status.HTTP_201_CREATED)

class MeanRetentionView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        doc_id = request.data["doc_id"]
        document = Document.objects.get(pk=int(doc_id))
        document_path, _ = os.path.splitext(document.document.path)
        document_media_path, _ = os.path.splitext(str(document.document))

        # task3 function performs Operation3 on file and return dataset
        df = task3(document.document)

        # save excel file
        dffile_path = document_path+'output_meanretention.xlsx'
        df.to_excel(dffile_path)

        data = {
            'file_path':[
            (default_storage.url(document_media_path+'output_meanretention.xlsx'), 
            'Mean of all the metabolites which have same "Retention Time Roundoff"')]
            }
        return JsonResponse(data, status=status.HTTP_201_CREATED)