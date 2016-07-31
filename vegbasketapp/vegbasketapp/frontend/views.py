from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from vegbasketapp.content.tools import get_entry_by_vg_id, get_vs_entry_by_id, get_entry_by_slug
from vegbasketapp.home.metas import get_vsmeta
from vegbasketapp.content.models import VeggieSailorEntry

# Create your views here.

def index(request):
    """Main frontend view.
    """
    return render(request, 'frontend/index.html',rc)

def entry_example(request):
    """Example entry view with new layout.
    """
    return render(request, 'frontend/entry_example.html')

def get_meta_entry(request, vs_entry):
    """Get the meta enhanced by entry's context.
    """
    meta = get_vsmeta()
    meta.title = vs_entry.name
    meta.description = vs_entry.short_description
    meta.keywords = [ x.name for x in vs_entry.tags.all() ] + [ x.name for x in vs_entry.cuisines.all() ]
    meta.object_type = 'restaurant.restaurant'
    meta.url = request.build_absolute_uri(vs_entry.get_absolute_url())
    if len(vs_entry.get_images_height_400())>0:
        meta.image = request.build_absolute_uri(vs_entry.get_images_height_400()[0].photo.url)
    elif len(vs_entry.get_images_height_348())>0:
        meta.image = request.build_absolute_uri(vs_entry.get_images_height_348()[0].photo.url)
    return meta

def entry_slug(request, slug):
    """Entry by the slug.
    """
    try:
        vs_entry = get_entry_by_slug(slug)
    except ObjectDoesNotExist:
        raise Http404("Page not found...")
    possible_others = VeggieSailorEntry.objects.filter(region=vs_entry.region_id).exclude(id=vs_entry.id)[0:4]
    
    other_places  = []
    
    if possible_others.count()==4:
        other_places = possible_others
    
    
    meta = get_meta_entry(request, vs_entry)
    return render(request, 'frontend/entry_view.html',
                  {'entry':vs_entry,'meta':meta,
                   'other_places':other_places})


def entry_vg(request, entry_id):
    """Entry by vegguide id.
    """
    vs_entry = get_entry_by_vg_id(entry_id)
    return redirect(vs_entry)

def entry_vs(request, entry_id):
    """Entry by vegguide id.
    """

    vs_entry = get_vs_entry_by_id(entry_id)
    meta = get_meta_entry(request, vs_entry)
    
    possible_others = VeggieSailorEntry.objects.filter(region=vs_entry.region_id)[0:4]
    
    other_places  = []
    
    if possible_others.count()==4:
        other_places = possible_others
    
    
    return render(request, 'frontend/entry_view.html',
                  {'entry':vs_entry,'meta':meta,
                   'other_places':other_places})


def homepage_map(request):
    return render(request, 'frontend/homepage_maps.html')



