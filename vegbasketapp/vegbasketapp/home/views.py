from django.shortcuts import render
from vegbasketapp.home.metas import get_vsmeta
from vegbasketapp.content.models import VeggieSailorEntry

def index(request):
    
 
    vsmeta = get_vsmeta()
  
    
    latest_entries = VeggieSailorEntry.objects.all().order_by('-created')[0:20]    
    
    rc = {'latest_entries':latest_entries, 'meta':vsmeta}   
    return render(request, 'home/index_fd.html', rc)

def opensource(request):
    #meta = VSMeta()
    vsmeta = get_vsmeta()
    
    return render(request, 'home/opensource.html', {'meta':vsmeta})
    

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')