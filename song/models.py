from django.db import models
from artist.models import Artist
from album.models import Album
# Create your models here.
class Song(models.Model):
    title=models.CharField(max_length=500)
    slug=models.SlugField(max_length=500)

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
        max_length=10,
        choices=GENRE_CHOICES,
        default='pop',
    )

    artist=models.ForeignKey(Artist)
    album=models.ManyToManyField(Album)

    listens=models.BigIntegerField()
    loved=models.BigIntegerField()
    content=models.TextField()
    lyrics=models.TextField()

    timestamp=models.DateTimeField(auto_now_add=True)
    duration=models.DurationField()