import os

from django.test import TestCase
from album.models import Album
from artist.models import Artist
from django.contrib.auth.models import  User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


def get_test_image():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path=os.path.abspath(os.path.join(BASE_DIR, 'album_tests/test.jpg'))
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
        artist_obj=get_artist_obj_by_name('Conor Lalor','Dublin','Ireland')
        album_obj=Album.objects.create(
            name='Sing Street: First Gig',
            content = 'This is the first gig album of our local band in dublin called singstreet',
            image = get_test_image(),
            artist = artist_obj,
        )
        self.assertEqual(album_obj.name,'Sing Street: First Gig')
        self.assertEqual(album_obj.content,'This is the first gig album of our local band in dublin called singstreet')

    def test_default_parameters(self):
        artist_obj = get_artist_obj_by_name('Conor Lalor', 'Dublin', country='Ireland')
        album_obj = Album.objects.create(
            name='Sing Street: First Gig',
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj,
        )
        self.assertEqual(album_obj.listens,0)
        self.assertEqual(album_obj.loved,0)

    def test_artist_cannot_have_duplicate_albums(self):
        artist_obj=get_artist_obj_by_name()

        album_obj1 = Album.objects.create(
            name='Sing Street: First Gig',
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj,
        )

        with self.assertRaises(ValidationError):

            album_obj2 = Album(
                name='Sing Street: First Gig',
                content='This is the first gig album of our local band in dublin called singstreet',
                image=get_test_image(),
                artist=artist_obj,
            )
            album_obj2.full_clean()


    def test_different_artist_can_have_same_album_name(self):
        artist_obj1 = get_artist_obj_by_name()
        artist_obj2 = get_artist_obj_by_name(name='farhan')
        same_name='Sing Street: First Gig'
        album_obj1 = Album.objects.create(
            name=same_name,
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj1,
        )

        album_obj2 = Album.objects.create(
            name=same_name,
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj2,
        )

        self.assertEqual(album_obj2.name,album_obj1.name)

    def test_ordering_of_albums(self):

        artist_obj = get_artist_obj_by_name('Conor Lalor', 'Dublin', country='Ireland')
        album_obj1 = Album.objects.create(
            name='Sing Street: First Gig1',
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj,
        )

        album_obj2 = Album.objects.create(
            name='Sing Street: First Gig2',
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj,
        )
        album_obj3 = Album.objects.create(
            name='Sing Street: First Gig3',
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj,
        )
        album_obj4 = Album.objects.create(
            name='Sing Street: First Gig4',
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj,
        )


        self.assertEqual(list(Album.objects.all()),[album_obj4,album_obj3,album_obj2,album_obj1])

    def test_string_representation(self):
        artist_obj = get_artist_obj_by_name('Conor Lalor', 'Dublin', 'Ireland')
        album_obj = Album.objects.create(
            name='Sing Street: First Gig',
            content='This is the first gig album of our local band in dublin called singstreet',
            image=get_test_image(),
            artist=artist_obj,
        )
        self.assertEqual(str(album_obj),'Sing Street: First Gig')
