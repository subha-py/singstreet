import os

from django.test import TestCase
from album.models import Album
from artist.models import Artist
from song.models import Song,Membership
from django.contrib.auth.models import  User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError


def get_test_image():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path=os.path.abspath(os.path.join(BASE_DIR, 'song_tests/test.jpg'))
    image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
    return image
def get_test_song():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.abspath(os.path.join(BASE_DIR, 'song_tests/test.mp3'))
    afile = SimpleUploadedFile(name='test.mp3', content=open(file_path, 'rb').read(), content_type='audio/mp3')
    return afile
def get_album_obj_by_name(name='singstreet'):
    user_obj= User.objects.create_user(username=slugify(name),email='{name}@example.com'.format(name=name),password='{name}123'.format(name=name))
    artist_obj = Artist.objects.create(
        user=user_obj,
        image=get_test_image(),
    )
    album_obj = Album.objects.create(
        name=name,
        content='This is the first gig album of our local band in dublin called singstreet',
        image=get_test_image(),
        artist=artist_obj,
    )
    return album_obj
class SongModelTest(TestCase):

    def test_create_song_model(self):
        album_obj=get_album_obj_by_name()
        song_obj=Song.objects.create(
            name='Riddle of the model',
            file = get_test_song(),
            content ='This is a test content',
            lyrics = 'This is demo lyrics',
            duration = 600,
            genre='rock'
        )
        m1=Membership.objects.create(
            song=song_obj,
            album = album_obj,
        )
        self.assertEqual(song_obj.name,'Riddle of the model')

    def test_default_paramaters(self):
        album_obj = get_album_obj_by_name()
        song_obj = Song.objects.create(
            name='Riddle of the model',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
        )
        m1 = Membership.objects.create(
            song=song_obj,
            album=album_obj,
        )

        self.assertEqual(song_obj.listens,0)
        self.assertEqual(song_obj.loved, 0)
        self.assertEqual(song_obj.duration,0)

    def test_one_album_cannot_have_two_identical_song(self):
        album_obj = get_album_obj_by_name()
        song_obj = Song.objects.create(
            name='Riddle of the model',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
            duration=600,
        )
        m1 = Membership.objects.create(
            song=song_obj,
            album=album_obj,
        )
        with self.assertRaises(ValidationError):
            m2 = Membership(
                song=song_obj,
                album=album_obj,
            )
            m2.full_clean()
    def test_two_album_can_have_same_song(self):
        album_obj1 = get_album_obj_by_name()
        album_obj2 = get_album_obj_by_name('rock on - magic')
        song_obj = Song.objects.create(
            name='Riddle of the model',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
            duration=600,
        )
        m1 = Membership.objects.create(
            song=song_obj,
            album=album_obj1,
        )
        m2 = Membership.objects.create(
            song=song_obj,
            album=album_obj2,
        )

        self.assertIn(album_obj1,song_obj.album.all())
        self.assertIn(album_obj2, song_obj.album.all())

    def test_song_ordering(self):
        album_obj = get_album_obj_by_name()
        song_obj1 = Song.objects.create(
            name='Riddle of the model',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
            duration=600,
            genre='rock'
        )
        m1 = Membership.objects.create(
            song=song_obj1,
            album=album_obj,
        )
        song_obj2 = Song.objects.create(
            name='Riddle of the model2',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
            duration=600,
            genre='rock'
        )
        m1 = Membership.objects.create(
            song=song_obj2,
            album=album_obj,
        )
        song_obj3 = Song.objects.create(
            name='Riddle of the model3',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
            duration=600,
            genre='rock'
        )
        m1 = Membership.objects.create(
            song=song_obj3,
            album=album_obj,
        )
        song_obj4 = Song.objects.create(
            name='Riddle of the model4',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
            duration=600,
            genre='rock'
        )
        m1 = Membership.objects.create(
            song=song_obj4,
            album=album_obj,
        )

        self.assertEqual(list(Song.objects.all()), [song_obj4, song_obj3, song_obj2, song_obj1])

    def test_string_representation(self):
        album_obj = get_album_obj_by_name()
        song_obj = Song.objects.create(
            name='Riddle of the model',
            file=get_test_song(),
            content='This is a test content',
            lyrics='This is demo lyrics',
            duration=600,
            genre='rock'
        )
        m1 = Membership.objects.create(
            song=song_obj,
            album=album_obj,
        )
        self.assertEqual(str(song_obj), 'Riddle of the model')