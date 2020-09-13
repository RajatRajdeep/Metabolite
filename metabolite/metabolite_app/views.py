from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
import requests
from django.conf import settings

BASE_URL = settings.BASE_URL
MEDIA_ROOT = settings.MEDIA_ROOT
BASE_DIR = settings.BASE_DIR

def home(request):
    if request.method == 'POST':
        response = requests.post(BASE_URL+'/upload', files={'document':request.FILES['document']})
        if response.status_code == 201:
            request.session["document"] = MEDIA_ROOT+response.json()['document']
            return redirect('tasks')
    
    form = DocumentForm()
    return render(request, 'metabolite_app/home.html', {
        'form': form
    })

def tasks(request):
    if request.method == 'GET':
        print(BASE_DIR,BASE_URL,MEDIA_ROOT)
        return render(request, 'metabolite_app/tasks.html')