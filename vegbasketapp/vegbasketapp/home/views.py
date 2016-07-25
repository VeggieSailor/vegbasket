from django.shortcuts import render
from vegbasketapp.home.metas import get_vsmeta
from vegbasketapp.content.models import VeggieSailorEntry

GOOD_ENTRIES = [85, 87, 86, 146, 278, 311, 772, 758, 837, 821, 843, 1417, 1428,
                1434, 1544, 1977, 2031, 1983, 2017, 2043, 2086, 2184, 2533,
                2410, 2552, 2594, 2696, 2715, 2708, 2815, 3003, 3015, 2961,
                3204, 3259, 3256, 5544, 3281, 1440, 3337, 3668, 3835, 3865,
                3892, 4081, 4118, 4121, 4190, 4260, 4409, 4434, 4438, 4480,
                4581, 4649, 4673, 4741, 4940, 4959, 4941, 5189, 5415, 5416,
                5417, 5439, 5494, 5549, 5529, 5569, 5655, 5620, 5651, 5773,
                5782, 5823, 6005, 5957, 5940, 6132, 6223, 113, 6558, 6617,
                6721, 6836, 6801, 6832, 6922, 6955, 6957, 7182, 7616, 7696,
                7973, 7995, 8063, 8516, 8541, 9070, 9437, 9575, 9585, 9653,
                9643, 9655, 8118, 1812, 4917, 9656, 9666, 5412, 4657, 4307,
                877, 4798, 4582, 2797, 135, 3215, 4361, 3649, 4401, 4327,
                4833, 7136, 7623, 6410, 6527, 691, 8024, 1842, 1867, 2053,
                611, 835, 8491, 4661, 322, 2219, 5728, 2388, 3288, 5822,
                6472, 239, 484, 9780, 811, 656, 1976, 4269, 1439, 7818,
                9667, 9654, 6106, 4345, 3454, 1742, 3316, 688, 4305, 4455,
                5302, 5333, 4948, 5407, 5923, 6279, 6925, 7433, 8242, 9699,
                9708, 9777, 9689, 8426, 9800, 492, 1355, 1552, 1662, 1694,
                1999, 2178, 2212, 2674, 2773, 2963, 3325, 4424, 5354, 5414,
                6245, 8352, 9668, 2055, 2128, 4397, 4491, 5022, 5147, 341,
                2828, 9757, 2044, 3049, 4175, 5088, 4548, 4938, 4801, 4825,
                5370, 6533, 6954, 928, 8425, 6145, 9797]


import random

def index(request):
    """Home page with hardcoded ids.
    
    Notes
    -----
    TODO: Hardcoded notes must be replaced.
    """

    places_ids = random.sample(GOOD_ENTRIES, 16)
    #places = VeggieSailorEntry.objects.filter(id__in=GOOD_ENTRIES)
    
    vsmeta = get_vsmeta()
    latest_entries = VeggieSailorEntry.objects.all().order_by('-created')[0:20]
    rc = {'latest_entries':latest_entries, 'meta':vsmeta,
          'places':places_ids}   
    return render(request, 'home/index_fd.html', rc)

def opensource(request):
    #meta = VSMeta()
    vsmeta = get_vsmeta()
    
    return render(request, 'home/opensource.html', {'meta':vsmeta})
    

def handler404(request):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')

