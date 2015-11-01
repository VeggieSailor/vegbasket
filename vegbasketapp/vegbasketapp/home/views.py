from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')