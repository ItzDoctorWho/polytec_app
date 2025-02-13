from django.db import models
from uuid import uuid4

def upload_picture(instance, filename):
    ext = filename.split('.')[-1]
    return 'static/uploads/members/{}.{}'.format(uuid4().hex, ext)

# Create your models here.
class Member(models.Model): 
    full_name = models.CharField(max_length=255) 
    email = models.EmailField(unique=True) 
    title = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True) 
    linkedin = models.CharField(max_length=255, null=True, blank=True) 
    facebook = models.CharField(max_length=255, null=True, blank=True) 
    website = models.CharField(max_length=255, null=True, blank=True) 
    picture = models.FileField(upload_to=upload_picture, null=True, blank=True)
    def __str__(self): 
        return self.full_name
