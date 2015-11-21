
import json
import requests
import tempfile
from hashlib import md5

from django.core import files

from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorEntry, VeggieSailorImage, \
     VeggieSailorCategory, VeggieSailorCuisine, VeggieSailorTag, VeggieSailorPayment
from vegbasketapp.transformer.models import Region, Entry
from vegbasketapp.transformer.tools_entry import get_region_by_id, get_entry_by_id
from django.contrib.contenttypes.models import ContentType

def get_region_id(url):
    """Extract id of the region.
    
    """
    return url.split('/')[-1]

def convert_region(region_id):
    vg_region_type = ContentType.objects.get(app_label="transformer", model="region")
    vg_entry_type = ContentType.objects.get(app_label="transformer", model="entry")    
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
    try:
        vs_region.name = region.obj['name']
    except KeyError:
        from ipdb import set_trace; set_trace()
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
    vg_region_type = ContentType.objects.get(app_label="transformer", model="region")
    vg_entry_type = ContentType.objects.get(app_label="transformer", model="entry")    
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
    vg_region_type = ContentType.objects.get(app_label="transformer", model="region")
    vg_entry_type = ContentType.objects.get(app_label="transformer", model="entry")    
    vg_entry = get_entry_by_id(entry_id)    
    vg_region = vg_entry.region
    print ("Region", vg_region.source_id)
      
    try:
        vs_entry= VeggieSailorEntry.objects.get(content_type=vg_entry_type, object_id=vg_entry.id)
    except VeggieSailorEntry.DoesNotExist:
        vs_entry= VeggieSailorEntry(content_type=vg_entry_type, object_id=vg_entry.id)
        
    try:
        vs_region = VeggieSailorRegion.objects.get(content_type=vg_region_type, object_id=vg_region.source_id)
    except VeggieSailorRegion.DoesNotExist:
        vs_region = convert_region(vg_region.source_id)
        
    vs_entry.name = vg_entry.get_name()
    vs_entry.region =  vs_region
    vs_entry.short_description = vg_entry.get_short_description()
    vs_entry.city = vg_entry.get_elem('city')
    vs_entry.address1 = vg_entry.get_elem('address1')
    vs_entry.address2 = vg_entry.get_elem('address2')
    vs_entry.vg_object_id = vg_entry.source_id


    vs_entry.level = vg_entry.get_elem('veg_level')
    
    price_range = vg_entry.get_elem('price_range')
    
    if price_range == '$ - inexpensive':
        price = 1
    elif price_range == '$$ - average':
        price = 2
    elif price_range == '$$$ - expensive':
        price = 3
    else:
        price = 0
        
    vs_entry.price = price
    
    print (price, price_range)

    # List of images to download
    image_urls = []
    
    
    vs_entry.description = vg_entry.get_long_description()
    vs_entry.zipcode = vg_entry.get_postal_code()
    
    
    #print ("smokesy",vg_entry.get_elem('allows_smoking'))
    vs_entry.allows_smoking = vg_entry.get_elem('allows_smoking')
    vs_entry.allows_reservations = vg_entry.get_elem('accepts_reservations')
    
    
    
    vs_entry.save()
    
    categories = vg_entry.get_elem('categories', [])
    vs_categories = []
    for category in categories:
        vs_category, created = VeggieSailorCategory.objects.get_or_create(name=category)        
        vs_categories.append(vs_category)
    
    if categories:
        vs_entry.categories = vs_categories
        vs_entry.save()
            
    cuisines = vg_entry.get_elem('cuisines',[])    
    vs_cuisines = []
    for cuisine in cuisines:
        vs_cuisine, created = VeggieSailorCuisine.objects.get_or_create(name=cuisine)
        vs_cuisines.append(vs_cuisine)
        
    if cuisines:
        vs_entry.cuisines = vs_cuisines
        vs_entry.save()

        cuisines = vg_entry.get_elem('cuisines',[])    
        vs_cuisines = []
        for cuisine in cuisines:
            vs_cuisine, created = VeggieSailorCuisine.objects.get_or_create(name=cuisine)
            vs_cuisines.append(vs_cuisine)
            
        if cuisines:
            vs_entry.cuisines = vs_cuisines
            vs_entry.save()

        
    tags = vg_entry.get_elem('tags',[])    
    vs_tags = []
    for tag in tags:
        vs_tag, created = VeggieSailorTag.objects.get_or_create(name=tag)
        vs_tags.append(vs_tag)
        
    if tags:
        vs_entry.tags = vs_tags
        vs_entry.save()

        tags = vg_entry.get_elem('tags',[])    
        vs_tags = []
        for tag in tags:
            vs_tag, created = VeggieSailorTag.objects.get_or_create(name=tag)
            vs_tags.append(vs_tag)
            
        if tags:
            vs_entry.tags = vs_tags
            vs_entry.save()

        
    payments = vg_entry.get_elem('payment_options',[])    
    print ("payments",payments)
    vs_payments = []
    for payment in payments:
        vs_payment, created = VeggieSailorPayment.objects.get_or_create(name=payment)
        vs_payments.append(vs_payment)
        
    if payments:
        vs_entry.payments = vs_payments
        vs_entry.save()

        payments = vg_entry.get_elem('payments',[])    
        vs_payments = []
        for payment in payments:
            vs_payment, created = VeggieSailorPayment.objects.get_or_create(name=payment)
            vs_payments.append(vs_payment)
            
        if payments:
            vs_entry.payments = vs_payments
            vs_entry.save()

        
    
    images = []
    
    VeggieSailorImage.objects.filter(entry=vs_entry).delete()
    
    images_list = [x for x in vg_entry.get_elem('images',[]) ]
    print ("images", images_list)
    # http://stackoverflow.com/questions/16174022/download-a-remote-image-and-save-it-to-a-django-model
    for image_elem in images_list:
        # Steam the image from the url
        try:
            title = image_elem['caption']
            for image_file in image_elem['files']:
                print (image_file)                
                image_url = image_file['uri']
                new_name = md5(image_url.encode('utf-8')).hexdigest()            
                request = requests.get(image_url, stream=True)            
                width = image_file['width']
                height = image_file['height']            
                # Was the request OK?
                if request.status_code != requests.codes.ok:
                    # Nope, error handling, skip file etc etc etc
                    continue
            
                # Get the filename from the url, used for saving later
                url_file_name_ext = image_url.split('/')[-1].split(".")[-1]
                
                file_name = '%s.%s' % (new_name, url_file_name_ext)
                # Create a temporary file
                lf = tempfile.NamedTemporaryFile()
            
                # Read the streamed image in sections
                for block in request.iter_content(1024 * 8):
            
                    # If no more file then stop
                    if not block:
                        break
            
                    # Write image block to temporary file
                    lf.write(block)
            
                # Create the model you want to save the image to
                image = VeggieSailorImage()
                image.title = title
                image.entry = vs_entry
                image.width = width
                image.height = height
                
            
                # Save the temporary image to the model#
                # This saves the model so be sure that is it valid
                image.photo.save(file_name, files.File(lf))    
                image.save()
        except KeyError:
            pass
    print(VeggieSailorEntry.objects.all().count())
    return vs_entry
      
def get_entry_by_vg_id(entry_id):
    """Get entry by VegGuide id.
    
    """
    vg_region_type = ContentType.objects.get(app_label="transformer", model="region")
    vg_entry_type = ContentType.objects.get(app_label="transformer", model="entry")       
    #try:
        #vs_entry= VeggieSailorEntry.objects.get(content_type=vg_entry_type, object_id=entry_id)
    #except VeggieSailorEntry.DoesNotExist:
    vs_entry = convert_entry(entry_id)
    
    return vs_entry
        
def get_vs_entry_by_id(entry_id)        :
    """Get entry by id.
    
    """
    entry = VeggieSailorEntry.objects.get(id = entry_id)
    return entry
        
        