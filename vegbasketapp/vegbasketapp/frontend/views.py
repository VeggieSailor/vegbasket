from django.shortcuts import render, redirect
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from vegbasketapp.content.tools import get_entry_by_vg_id, get_vs_entry_by_id, get_entry_by_slug
from vegbasketapp.home.metas import get_vsmeta
from vegbasketapp.content.models import VeggieSailorEntry
from django.shortcuts import HttpResponseRedirect


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
    
    
    
    if request.user.is_authenticated():    
        amount = vs_entry.visit_set.filter(user=request.user).count()
        
        visited_txt = "YOUR VISITS: %d" % amount
    else:
        visited_txt = "YOUR VISITS: 0"
    
    
    meta = get_meta_entry(request, vs_entry)
    return render(request, 'frontend/entry_view.html',
                  {'entry':vs_entry,'meta':meta,
                   'other_places':other_places,
                   'visited_txt':visited_txt,
                   'price_list':range(0,vs_entry.price)})


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





from vegbasketapp.content.tools import convert_entry

from vegbasketapp.transformer.models import Entry

from django.conf import settings
from django.contrib.auth.decorators import permission_required
from vegbasketapp.transformer.tools_entry import get_entry_by_id, \
     get_reviews_by_entry_id, get_region_by_id, get_entry_geo
@permission_required('content.change_veggiesailorentry')
def convert_entry_vg(request, slug):
    try:
        vs_entry = get_entry_by_slug(slug)
    except ObjectDoesNotExist:
        raise Http404("Page not found...")
    source_id = vs_entry.content_object.source_id
    entry_tmp = get_entry_by_id(source_id, True)
    entry_tmp.set_obj()    
    obj_id = vs_entry.id
    convert_entry(source_id, True)
    new_vs = VeggieSailorEntry.objects.get(id=obj_id)
    return HttpResponseRedirect(new_vs.get_absolute_url())
    

