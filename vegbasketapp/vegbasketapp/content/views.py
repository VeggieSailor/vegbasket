from django.shortcuts import render

# Create your views here.

def trans(request):
    return render(request, "trans.html")