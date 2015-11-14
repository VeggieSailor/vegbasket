from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorEntry
from vegbasketapp.transformer.models import Region
from vegbasketapp.transformer.tools_entry import get_region_by_id
import json

from django.contrib.contenttypes.models import ContentType
region_type = ContentType.objects.get(app_label="transformer", model="region")

def get_region_id(url):
    """Extrac id of the region.
    
    """
    return url.split('/')[-1]


def convert_region(region_id):
    
    try:
        region = Region.objects.get(source_id=region_id)
    except Region.DoesNotExist:
        region = get_region_by_id(region_id)    
    region.set_obj()    
    
    if VeggieSailorRegion.objects.filter(source_region=region).count()>0:
        vs_region = VeggieSailorRegion.objects.get(source_region=region)
        vs_region.content_type = region_type
        vs_region.object_id = region.source_id        
        vs_region.save()
        return vs_region

    vs_region = VeggieSailorRegion()
    vs_region.name = region.obj['name']
    vs_region.content_type = region_type
    vs_region.object_id = region.source_id
    vs_region.source_region = region
    vs_region.save()
    
    if 'parent' in region.obj and 'uri' in region.obj['parent']:
        parent_id = get_region_id(region.obj['parent']['uri'])
        print ("has parent", region_id, parent_id)
        vs_region_parent = convert_region(parent_id)
        vs_region.parent = vs_region_parent
        vs_region.save()
    
    return vs_region


def convert_region_down(region_id, global_list=[]):
    """Convert region.

    Parameters
    ----------
    region_id
    """
    print ("current region ", region_id, global_list)

    
    if region_id  in global_list:
        print ("Leaving", region_id)
        return None
        
    vs_region = convert_region(region_id)

    global_list.append(region_id)    
    region = Region.objects.get(source_id=region_id)
    try:
        region = Region.objects.get(source_id=region_id)
    except Region.DoesNotExist:
        region = get_region_by_id(region_id)
    print (region)
    
    children = region.get_children()
    print (region_id, children)    
    #if region.parent_id:
        #convert_region_down(parent_id, global_list)
    
    for child in children:
        print ("doing child", child)
        convert_region_down(int(child), global_list)
    
    
    #from ipdb import set_trace; set_trace()
    #if region.obj.has_key('children'):
        #for child in obj['children']:
            #print child['url']
    
        
    
    
    return (region, vs_region)
    