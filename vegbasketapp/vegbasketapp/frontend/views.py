from django.shortcuts import render

from vegbasketapp.content.tools import get_entry_by_vg_id, get_vs_entry_by_id


# Create your views here.

def index(request):
    """Main frontend view.
    
    """
    return render(request, 'frontend/index.html')

def entry_example(request):
    """Example entry view with new layout.
    
    """
    return render(request, 'frontend/entry_example.html')


def entry_vg(request, entry_id):
    """Entry by vegguide id.
    
    """
    vs_entry = get_entry_by_vg_id(entry_id)
    return render(request, 'frontend/entry_view.html',
                  {'entry':vs_entry})

def entry_vs(request, entry_id):
    """Entry by vegguide id.
    
    """
    
    
    
    
    vs_entry = get_vs_entry_by_id(entry_id)
    
    meta = dict(use_og=True,use_twitter=True)
    
    meta['title'] = vs_entry.name
    meta['site_name'] = 'Veggie Sailor'
    meta['description'] = vs_entry.short_description
    meta['keywords'] = [ x.name for x in vs_entry.tags.all() ] + [ x.name for x in vs_entry.cuisines.all() ]
    meta['object_type'] = 'restaurant.restaurant'
    meta['twitter_site'] = '@veggiesailor'
    meta['twitter_card'] = 'summary'
    meta['url'] = request.build_absolute_uri(vs_entry.get_absolute_url())
     
    try:
        meta['image'] = request.build_absolute_uri(vs_entry.get_images_height_400()[0].photo.url) 
    except IndexError:
        meta['image'] = 'https://veggiesailor.com/static/frontend/img/logo.png'
        
    
    return render(request, 'frontend/entry_view.html',
                  {'entry':vs_entry,'meta':meta})