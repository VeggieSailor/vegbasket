from vegbasketapp.content.models import VeggieSailorRegion, VeggieSailorEntry
from vegbasketapp.transformer.models import Region
import json

def convert_region(region_id):
    """Convert region.

    Parameters
    ----------
    region_id
    """
    region = Region.objects.get(source_id=region_id)
    region.set_obj()
    vs_region = VeggieSailorRegion()
    vs_region.name = region.obj['name']
    vs_region.save()
    return (region, vs_region)
    