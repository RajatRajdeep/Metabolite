from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
from .models import Document
import requests

BASE_URL = 'http://127.0.0.1:8000'

def home(request):
    if request.method == 'POST':
        response = requests.post(BASE_URL+'/upload', files={'document':request.FILES['document']})
        if response.status_code == 201:
            return HttpResponse('Yay, it worked')
    
    form = DocumentForm()
    return render(request, 'metabolite_app/home.html', {
        'form': form
    })