from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    profile = models.ImageField(default='avatar.svg')




class TourismCartegory(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    

class About(models.Model):
    goal = models.TextField()
    passion = models.TextField()
    work = models.TextField()


class Destination(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    pics = models.ImageField(null=True)
    top = models.ForeignKey(TourismCartegory, on_delete=models.CASCADE)
    country_namw = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.country_namw
    

class Post(models.Model):
    topic = models.ForeignKey(TourismCartegory, on_delete=models.SET_NULL, null=True)
    country_name = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)
    pics = models.ImageField(null=True) 
    picsd = models.ImageField(null=True) 
    picsf = models.ImageField(null=True) 

    def __str__(self):
        return self.country_name
    
class Comments(models.Model):
    bloo = models.ForeignKey(Destination, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    