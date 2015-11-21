
import datetime
from haystack import indexes
from vegbasketapp.content.models import VeggieSailorEntry

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return VeggieSailorEntry
    
    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
    #def index_queryset(self, using=None):
        #"""Used when the entire index for model is updated."""
        #return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())