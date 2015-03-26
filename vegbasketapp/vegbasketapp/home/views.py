from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')
    # return render(request, 'base.html')
