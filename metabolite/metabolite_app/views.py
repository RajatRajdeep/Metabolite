from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DocumentForm
import requests
from metabolite.settings import BASE_URL

def home(request):
    if request.method == 'POST':
        response = requests.post(BASE_URL+'/upload', files={'document':request.FILES['document']})
        if response.status_code == 201:
            # Document id stored in session
            request.session["doc_id"] = response.json()['id']
            return redirect('tasks')
        else:
            context = response.json()

    if request.method == 'GET':
        # Reset Document id stored in session
        request.session["doc_id"] = None
        context = {}
    
    context['form'] = DocumentForm()
    return render(request, 'metabolite_app/home.html', context=context)
    
def tasks(request):
    if request.method == 'GET':
        if request.session.get("doc_id", False):
            return render(request, 'metabolite_app/tasks.html')
        else:
            return redirect('home')

def showresult(request, task_id):
    if request.method == 'GET':
        
        # Redirect to home page if request url is invalid
        if not request.session.get("doc_id", False) or task_id not in [1,2,3]:
            return redirect('home')

        # Post request for different operations to get response
        if task_id==1:
            response = requests.post(BASE_URL+'/filter_metabolites', data = {'doc_id':request.session["doc_id"]})
            context = response.json()
        elif task_id==2:
            response = requests.post(BASE_URL+'/roundoff_retention', data = {'doc_id':request.session["doc_id"]})
            context = response.json()
        elif task_id==3:
            response = requests.post(BASE_URL+'/mean_retention', data = {'doc_id':request.session["doc_id"]})
            context = response.json()

        if response.status_code == 201:
                return render(request, 'metabolite_app/tasks.html', context=context)