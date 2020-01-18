from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from django.db import models

class Room(models.Model):
    """Represents chat rooms that users can join"""

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)
    startup =  models.TextField()
    mentor = models.TextField()

    def __str__(self):
        """Returns human-readable representation of the model instance."""
        return self.name