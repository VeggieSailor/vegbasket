from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorEntry
from vegbasketapp.transformer.models import Region
import json

def get_region_id(url):
    return url.split('/')[-1]



def convert_region_down(region_id, global_list=[]):
    """Convert region.

    Parameters
    ----------
    region_id
    """
    region = Region.objects.get(source_id=region_id)
    region.set_obj()
    
    
    if region_id  in global_list:
        return None
    
        
    
    #if region.obj.has_key('children'):
        #for child in obj['children']:
            #print child['url']
    
    from ipdb import set_trace; set_trace()
    
    vs_region = VeggieSailorRegion()
    vs_region.name = region.obj['name']
    vs_region.save()
    global_list.append(region_id)
    return (region, vs_region)
    