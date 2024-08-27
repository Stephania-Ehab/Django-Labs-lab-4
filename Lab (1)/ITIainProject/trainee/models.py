from django.shortcuts import redirect
from django.urls import reverse
from django.db import models
from track.models import *

# Create your models here.

class Trainee(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False)
    image=models.ImageField(upload_to='trainee/images/',blank=True,null=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    phone = models.IntegerField()
    trackobj=models.ForeignKey("track.Track",on_delete=models.CASCADE )

    def getimage(self):
        return f'/media/{self.image}'

    def get_list_url():
        return reverse('trainee_list')
    
    @classmethod
    def create(cls,name,image,email,age,phone,trackid):
        traineeobj = Trainee() 
        traineeobj.name= name
        traineeobj.image= image
        traineeobj.email= email
        traineeobj.age= age
        traineeobj.phone= phone
        traineeobj.trackobj=Track.objects.get(pk=trackid)
        traineeobj.save()
        return redirect(cls.get_list_url())