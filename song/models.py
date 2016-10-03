from django.db import models


from album.models import Album
from autoslug import AutoSlugField
import datetime

def song_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/year/month/date/genre/slug
    now=datetime.datetime.now()
    return 'song/{genre}/{year}/{month}/{date}/{slug}'.format(
        genre=instance.genre,
        slug=instance.slug,
        year=now.year,month=now.month,date=now.day
    )


class Song(models.Model):
    name=models.CharField(max_length=500)
    slug=AutoSlugField(populate_from='name', unique=True)

    GENRE_CHOICES = (
        ('blues','Blues'),
        ('comedy','Comedy'),
        ('country','Country'),
        ('easy','Easy Listening'),
        ('edm','EDM'),
        ('folk','Folk'),
        ('hiphop','Hip-Hop'),
        ('jazz','Jazz'),
        ('pop','Pop'),
        ('rnb','R&B and soul'),
        ('rock','Rock'),
    )

    genre = models.CharField(
        max_length=200,
        choices=GENRE_CHOICES,
        default='pop',
    )
    file= models.FileField(upload_to=song_directory_path,null=True)
    album=models.ManyToManyField(Album,through='Membership')

    listens=models.BigIntegerField(default=0)
    loved=models.BigIntegerField(default=0)
    content=models.TextField(blank=True)
    lyrics=models.TextField(blank=True)

    timestamp=models.DateTimeField(auto_now_add=True)

    #duration will always be in seconds
    duration=models.IntegerField(default=0)

    class Meta:
        ordering=['-timestamp']

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Membership(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=['song','album']
