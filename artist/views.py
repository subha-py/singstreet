from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.shortcuts import render,redirect
from artist.forms import ArtistForm,UserForm
# Create your views here.
def create_artist(request):
    userform=UserForm(request.POST or None,prefix='user')
    artistform=ArtistForm(request.POST or None,request.FILES or None,prefix='artist')
    if userform.is_valid() and artistform.is_valid():
        user = userform.save(commit=False)
        password = userform.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        artistform.save(for_user=new_user)
        return redirect('/')
    else:
        context={
            'userform':userform,
            'artistform':artistform,
        }
        return render(request,'artist_create.html',context)

def view_artist(request,slug):
    pass

def delete_artist(request,slug):
    pass

def login_artist(request):
    pass