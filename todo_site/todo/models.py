from django.db import models
from django.utils import timezone

# the name of our table is "todo"
class Todo(models.Model):            
        title=models.CharField(max_length=100)  # create column "title"
        details=models.TextField()              # create column "details"
        date=models.DateTimeField(default=timezone.now)    # create column "date"
        
        # no need to create an entry for primary_id
        # django will take care of this

        def __str__(self):
                return self.title

