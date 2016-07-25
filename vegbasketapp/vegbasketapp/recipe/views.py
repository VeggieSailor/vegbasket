from django.shortcuts import render

# Create your views here.

def recipe_french_pate(request):
    return render(request, "recipe/french_pate.html")