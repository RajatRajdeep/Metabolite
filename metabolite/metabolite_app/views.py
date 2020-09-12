from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

def home(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'metabolite_app/home.html', {
        'form': form
    })
