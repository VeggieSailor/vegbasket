from django.shortcuts import render
from vegbasketapp.home.metas import get_vsmeta
def index(request):
    
 
    vsmeta = get_vsmeta()
  
   
    return render(request, 'home/index_fd.html', {'meta':vsmeta})

def opensource(request):
    #meta = VSMeta()
    vsmeta = get_vsmeta()
    
    return render(request, 'home/opensource.html', {'meta':vsmeta})
    

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')