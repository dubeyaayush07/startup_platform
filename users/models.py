from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('EAD', 'Engineering & Data'),
    ('DESIGN', 'Design'),
    ('BUS', 'Business'),
    ('OTHER', 'other'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_mentor = models.BooleanField(default=False)
    description = models.TextField
    category = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='EAD')

    def __str__(self):
        return f'{self.user.username} Profile'

      


