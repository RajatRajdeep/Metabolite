from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

BASE_URL = settings.BASE_URL

@csrf_exempt
def home(request):
    if request.method == 'POST':
        response = requests.post(BASE_URL+'/upload', files={'document':request.FILES['document']})
        if response.status_code == 201:
            request.session["document"] = response.json()['document']
            return redirect('tasks')
    form = DocumentForm()
    return render(request, 'metabolite_app/home.html', {
        'form': form
    })

def tasks(request):
    if request.method == 'GET':
        context={}
        context["path"] = []
        return render(request, 'metabolite_app/tasks.html', context=context)

def showresult(request, task_id):
    if request.method == 'GET':
        if task_id==1:
            response = requests.post(BASE_URL+'/filter_metabolites', data = {'document':request.session["document"]})
            context = response.json()
        elif task_id==2:
            response = requests.post(BASE_URL+'/roundoff_retention', data = {'document':request.session["document"]})
            context = response.json()
        elif task_id==3:
            response = requests.post(BASE_URL+'/mean_retention', data = {'document':request.session["document"]})
            context = response.json()
        else:
            return HttpResponse('Invalid Request')
        if response.status_code == 201:
                return render(request, 'metabolite_app/tasks.html', context=context)