import os

from django.test import TestCase
from album.models import Album
from artist.models import Artist
from django.contrib.auth.models import  User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import slugify

def get_test_image():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path=os.path.abspath(os.path.join(BASE_DIR, 'static/img/test.jpg'))
    image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
    return image
def get_artist_obj_by_name(name='elspeth',location='Athens',country='Greece',):
    user_obj= User.objects.create_user(username=slugify(name),email='{name}@example.com'.format(name=name),password='{name}123'.format(name=name))
    artist_obj = Artist.objects.create(
        user=user_obj,
        image=get_test_image(),
        location=location,
        country=country,
    )
    return artist_obj
class AlbumModelTest(TestCase):

    def test_album_create(self):
        artist_obj=get_artist_obj_by_name('Conor Lalor','Dublin',country='Ireland')
        album_obj=Album.objects.create(
            name='Sing Street: First Gig',
            content = 'This is the first gig album of our local band in dublin called singstreet',
            image = get_test_image(),
            artist = artist_obj,
        )
        self.assertEqual(album_obj.name,'Sing Street: First Gig')
        self.assertEqual(album_obj.content,'This is the first gig album of our local band in dublin called singstreet')