from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorEntry
from vegbasketapp.transformer.models import Region
from vegbasketapp.transformer.tools_entry import get_region_by_id, get_entry_by_id
import json

from django.contrib.contenttypes.models import ContentType

vg_region_type = ContentType.objects.get(app_label="transformer", model="region")
vg_entry_type = ContentType.objects.get(app_label="transformer", model="entry")

def get_region_id(url):
    """Extract id of the region.
    
    """
    return url.split('/')[-1]


def convert_region(region_id):
    """Convert single region and it's parent.
    
    Notes
    -----
        Works in the recursive way.
        
    """
    
    try:
        region = Region.objects.get(source_id=region_id)
    except Region.DoesNotExist:
        region = get_region_by_id(region_id)    
    region.set_obj()    
    
    if VeggieSailorRegion.objects.filter(source_region=region).count()>0:
        vs_region = VeggieSailorRegion.objects.get(source_region=region)
        vs_region.content_type = vg_region_type
        vs_region.object_id = region.source_id        
        vs_region.save()
        return vs_region

    vs_region = VeggieSailorRegion()
    vs_region.name = region.obj['name']
    vs_region.content_type = vg_region_type
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
    
    for child in children:
        print ("doing child", child)
        convert_region_down(int(child), global_list)
   
    return (region, vs_region)
    
    
def convert_entry(entry_id):
    """Convert entry to the VeggieSailor object.
    
    """
    vg_entry = get_entry_by_id(entry_id)    
    vg_region = vg_entry.region
      
    try:
        vs_entry= VeggieSailorEntry.objects.get(content_type=vg_entry_type, object_id=vg_entry.id)
    except VeggieSailorEntry.DoesNotExist:
        vs_entry= VeggieSailorEntry(content_type=vg_entry_type, object_id=vg_entry.id)
        
    try:
        vs_region = VeggieSailorRegion.objects.get(content_type=vg_region_type, object_id=vg_region.id)
    except VeggieSailorRegion.DoesNotExist:
        vs_region = convert_region(vg_region.id)
        
    vs_entry.name = vg_entry.get_name()
    vs_entry.region =  vs_region
    
    vs_entry.save()
    
    print(VeggieSailorEntry.objects.all().count())
    return vs_entry
    
    
def get_entry_by_vg_id(entry_id):
    try:
        vs_entry= VeggieSailorEntry.objects.get(content_type=vg_entry_type, object_id=entry_id)
    except VeggieSailorEntry.DoesNotExist:
        vs_entry = convert_entry(entry_id)
    
    return vs_entry
        
        
        