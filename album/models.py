from django.db import models
from artist.models import Artist

def album_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/album/album_slug
    return 'album/{0}'.format(instance.slug)
class Album(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    content=models.TextField()
    image=models.ImageField(upload_to=album_directory_path,null=True)
    loved=models.BigIntegerField(default=0)
    listens=models.BigIntegerField(default=0)
    artist=models.ForeignKey(Artist)