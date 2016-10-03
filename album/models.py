from django.db import models

from autoslug import AutoSlugField

from artist.models import Artist

def album_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/album/album_slug
    return 'album/{0}'.format(instance.slug)
class Album(models.Model):
    name=models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name', unique=True)
    content=models.TextField(blank=True)
    image=models.ImageField(upload_to=album_directory_path,null=True)
    loved=models.BigIntegerField(default=0)
    listens=models.BigIntegerField(default=0)
    artist=models.ForeignKey(Artist)

    timestamp = models.DateTimeField(auto_now_add=True)

    #duration will always be in seconds
    duration = models.IntegerField(default=0)
    class Meta:
        unique_together=['name','artist']
        ordering=['-timestamp']

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name