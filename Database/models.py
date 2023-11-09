from django.db import models

from django.contrib.auth.models import AbstractUser



# Create your models here.

class Students (models.Model):
    name = models.CharField(max_length=20,blank=False,)
    email=models.EmailField()
    phone=models.IntegerField()
    image=models.ImageField(upload_to="uploaded/images",default="profile.jpg")
    #dynamic admin page
    # font_size=models.IntegerField()

    def __str__(self):
        return self.name
    
class Sliders( models.Model):
    text = models.CharField(max_length=20,blank=False,null=False)
    text1= models.CharField(max_length=20,blank=False,null=False)
    image= models.ImageField(upload_to="uploads/sliders",default="uploads/sliders/profile.jpg") 

    def __str__(self):
        return self.text
    
class CustomUser(AbstractUser):
    year=models.PositiveBigIntegerField(blank=True,null=True)
