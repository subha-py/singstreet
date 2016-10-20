from django.test import TestCase
from django.contrib.auth import get_user_model

from artist.forms import UserForm,ArtistForm
from artist.models import Artist


class UserFormTest(TestCase):
