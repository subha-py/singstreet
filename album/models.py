from django.db import models
from artist.models import Artist
# Create your models here.

class Album(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    content=models.TextField()
    image=models.ImageField()
    artist=models.ForeignKey(Artist)