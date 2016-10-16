from django.contrib.auth import login
from .models import Artist
from django.shortcuts import render,redirect,get_object_or_404
from artist.forms import ArtistForm
from django.contrib.auth.backends import ModelBackend
from allauth.account.auth_backends import AuthenticationBackend



# Create your views here.

def signup_artist(request):
    return render(request,'artist_signup.html')

def login_artist(request):
    return render(request, 'artist_login.html')

def create_artist(request):
    user = request.user
    artist_qs = Artist.objects.filter(user__email=user.email)
    if artist_qs.exists():
        return redirect(artist_qs.first().get_absolute_url())
    print(user.email)
    artistform = ArtistForm(request.POST or None, request.FILES or None, prefix='artist')
    if artistform.is_valid():
        if user.username != artistform.cleaned_data.get('username'):
            user.username = artistform.cleaned_data.get('username')
            user.save()
            login(request,user)
        artist_obj = artistform.save(for_user=user)
        return redirect(artist_obj.get_absolute_url())
    else:
        context = {
            'artistform': artistform,
        }
        return render(request, 'artist_create.html', context)


def view_artist(request,username):
    artist_obj=get_object_or_404(Artist,user__username=username)
    context={
        'artist_obj':artist_obj,
    }
    return render(request,'artist_view.html',context)

def delete_artist(request,slug):
    pass