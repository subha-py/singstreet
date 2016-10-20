from django.contrib.auth import login
from .models import Artist
from django.shortcuts import render,redirect,get_object_or_404
from artist.forms import ArtistForm,UserForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.forms import ValidationError


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


@login_required(login_url='/artist/login/')
def update_artist(request):
    user = request.user
    artistform = ArtistForm(request.POST or None, request.FILES or None,
                            prefix='artist',instance=user.artist,
                            initial={'username':user.username}
                            )
    userform=UserForm(request.POST or None,request.FILES or None,prefix='user',instance=user)
    if artistform.is_valid() and userform.is_valid():
        first_name=userform.cleaned_data.get('first_name')
        user=userform.save()
        artist_obj = artistform.save(for_user=user)
        return redirect(artist_obj.get_absolute_url())
    else:
        context = {
            'artistform': artistform,
            'userform': userform,
        }
        return render(request, 'update_artist.html', context)

def delete_artist(request):
    user=request.user
    User=get_user_model()
    User.objects.get(username=user.username).delete()
    return redirect('/')