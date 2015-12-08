from django.shortcuts import render

def index(request):
    
    meta = dict(use_og=True,use_twitter=True)
    meta['title'] = "Welcome to Veggie Sailor"
    meta['site_name'] = 'Veggie Sailor'
    meta['description'] = "Vegetarian Vegan Open Data Platform"
    meta['keywords'] = ['vegeterian','vegan', 'bar', 'restaurant']
    meta['object_type'] = 'article'
    meta['twitter_site'] = '@veggiesailor'
    meta['twitter_card'] = 'summary'
    meta['url'] = 'https://veggiesailor.com'
    meta['image'] = 'https://veggiesailor.com/static/frontend/img/logo.png'    
    
    return render(request, 'home/index_fd.html', {'meta':meta})

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')