from django.db import models
from django.conf import settings


def artist_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist/artist_slug
    return 'artist/{0}.png'.format(instance.user.username)
class Artist(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=artist_directory_path,null=True,blank=True)
    country = models.CharField(max_length=255, default='india')
    location=models.CharField(max_length=255,default='kolkata')
    listens=models.BigIntegerField(default=0)
    loved=models.BigIntegerField(default=0)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username