from django.shortcuts import render
from .models import Recipe
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.list import ListView

### Depreceated

def recipe_french_pate(request):
    return render(request, "recipe/french_pate.html")

def mediterranean_tabbouleh_salad(request):
    return render(request, "recipe/tabbouleh.html")

def recipe_slug(request, slug):
    """Recipe by the slug.
    """
    try:
        vs_entry = get_entry_by_slug(slug)
    except ObjectDoesNotExist:
        raise Http404("Page not found...")

### New views

class RecipeDetailView(DetailView):

    model = Recipe
    slug_field = "slug"
    
    def get_queryset(self):
        return Recipe.objects.filter(active=True)
    
    def get_context_data(self, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class RecipeListView(ListView):

    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(active=True)

    def get_context_data(self, **kwargs):
        context = super(RecipeListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


