from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


def artist_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/artist/artist_slug
    return 'artist/{0}.png'.format(instance.user.username)


class Artist(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='artist')

    GENDER_CHOICES=(
        ('M','Male'),
        ('F','Female'),
        ('N','Neutral')
    )
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,blank=True,null=True)
    image=models.ImageField(upload_to=artist_directory_path,null=True,blank=True)
    country = models.CharField(max_length=255, default='japan')
    location=models.CharField(max_length=255,default='tokyo')
    listens=models.BigIntegerField(default=0)
    loved=models.BigIntegerField(default=0)
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("artist:view", kwargs={"username": self.user.username})