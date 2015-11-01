from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def entry_example(request):
    return render(request, 'frontend/entry_example.html')