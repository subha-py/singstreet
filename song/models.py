from django.db import models


from artist.models import Artist
from album.models import Album



def song_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/year/month/date/genre/slug
    return 'song/{0}/%Y/%m/%d/{1}'.format(instance.genre,instance.slug)

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
        max_length=200,
        choices=GENRE_CHOICES,
        default='pop',
    )
    file= models.FileField(upload_to=song_directory_path,null=True)
    artist=models.ForeignKey(Artist)
    album=models.ManyToManyField(Album)

    listens=models.BigIntegerField()
    loved=models.BigIntegerField()
    content=models.TextField()
    lyrics=models.TextField()

    timestamp=models.DateTimeField(auto_now_add=True)
    duration=models.DurationField()

