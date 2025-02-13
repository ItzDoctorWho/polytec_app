from django.db import models

# Create your models here.
class Member(models.Model): 
    full_name = models.CharField(max_length=255) 
    email = models.EmailField(unique=True) 
    title = models.CharField(max_length=255, null=True, blank=True)  # 🔥 Add title
    bio = models.TextField(null=True, blank=True)  # 🔥 Add bio
    city = models.CharField(max_length=255, null=True, blank=True)  # 🔥 Add city
    github = models.CharField(max_length=255, null=True, blank=True)  # 🔥 Add github
    instagram = models.CharField(max_length=255, null=True, blank=True)  # 🔥 Add instagram
    twitter = models.CharField(max_length=255, null=True, blank=True) 
    linkedin = models.CharField(max_length=255, null=True, blank=True) 
    facebook = models.CharField(max_length=255, null=True, blank=True) 
    website = models.CharField(max_length=255, null=True, blank=True) 
    picture = models.FileField(null=True, blank=True) 

    def __str__(self): 
        return self.full_name
