import os

from django.test import TestCase
from artist.models import Artist
from django.contrib.auth.models import  User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template.defaultfilters import slugify

def get_test_image():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    image_path=os.path.abspath(os.path.join(BASE_DIR, 'static/img/test/test.jpg'))
    image = SimpleUploadedFile(name='test_image.jpg', content=open(image_path, 'rb').read(), content_type='image/jpeg')
    return image
def get_user_obj_by_name(name='elspeth'):
    return User.objects.create_user(username=slugify(name),email='{name}@example.com'.format(name=name),password='{name}123'.format(name=name))

class ArtistModelTest(TestCase):

    def test_user_obj(self):
        name='elspeth'
        user_obj=get_user_obj_by_name(name)
        self.assertEqual(name,user_obj.username)

    def test_artist_creation(self):
        user_obj=get_user_obj_by_name('Conor Lalor')
        artist_obj=Artist.objects.create(
            user=user_obj,
            image = get_test_image(),
            location = 'Dublin',
            country = 'Ireland',
        )
        self.assertEqual(artist_obj.user.username,user_obj.username)
        self.assertEqual(artist_obj.country.lower(),'ireland')
        self.assertEqual(artist_obj.location.lower(),'dublin')

    def test_default_parameters(self):
        user_obj = get_user_obj_by_name('Farhan Akhtar')
        artist_obj = Artist.objects.create(
            user=user_obj,
            image=get_test_image(),
        )
        self.assertEqual(artist_obj.user.username, user_obj.username)
        self.assertEqual(artist_obj.country.lower(), 'india')
        self.assertEqual(artist_obj.location.lower(), 'kolkata')