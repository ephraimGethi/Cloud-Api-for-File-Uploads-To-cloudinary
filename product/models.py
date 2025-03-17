from django.db import models
from django.conf import settings
import cloudinary.models

class computer(models.Model):
    name = models.TextField()
    avatar = cloudinary.models.CloudinaryField("image", null=True, blank=True) 
    video = cloudinary.models.CloudinaryField("video", null=True, blank=True)  
    document = cloudinary.models.CloudinaryField("raw", null=True, blank=True,resource_type="raw") 
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def image_url(self):
        return self.avatar.url if self.avatar else None
    
    
    
class Rooms(models.Model):
    name = models.TextField()
    description = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
