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
    return render(request, 'frontend/entry_view.html',
                  {'entry':vs_entry})