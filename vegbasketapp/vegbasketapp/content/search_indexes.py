
import datetime
from haystack import indexes
from vegbasketapp.content.models import VeggieSailorEntry

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    """Default index for the entry.
    
    """
    text = indexes.CharField(document=True, use_template=True)
    level = indexes.IntegerField(model_attr='level')
    photos = indexes.IntegerField()
    rating = indexes.FloatField(model_attr='rating')
    mod_date = indexes.DateTimeField(model_attr='modified')
    location = indexes.LocationField(model_attr='get_location')

    def get_updated_field(self):
        return 'modified'
    
    def get_model(self):
        """Get the model.
        
        """
        return VeggieSailorEntry
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated.
        
        """
        return self.get_model().objects.filter(active=True)
    
    def prepare_photos(self, obj):
        """Count number of the images for the entry.
        """
        return int(obj.veggiesailorimage_set.count())
        
