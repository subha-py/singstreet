from django.db import models
from django.conf import settings
# Create your models here.
class Artist(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    slug=models.SlugField()
    image=models.ImageField()
    location=models.CharField(max_length=255)
    country=models.CharField(max_length=255)
    listens=models.BigIntegerField()
    loved=models.BigIntegerField()
    #albums=models.ForeignKey()
    timestamp=models.DateTimeField(auto_now_add=True)
