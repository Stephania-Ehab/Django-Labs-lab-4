from django.db import models
from django.urls import reverse

# Create your models here.

class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)

    @classmethod
    def getall(cls):
        return [(track.id,track.name) for track in cls.objects.all()]