from django.db import models
from django.contrib.auth.models import User

# Create your models here.

CATEGORY_CHOICES = (
    ('EAD', 'Engineering & Data'),
    ('DESIGN', 'Design'),
    ('BUS', 'Business'),
    ('OTHER', 'other'),
)


ROLE_CHOICES = (
    ('M', 'Mentor'),
    ('S', 'Startup'),
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='S')
    description = models.TextField()
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='EAD')
    



    def __str__(self):
        return f'{self.user.username} Profile'

      


