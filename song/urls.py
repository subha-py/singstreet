from django.conf.urls import url

from song.views import create_song,view_song,delete_song

urlpatterns = [
    # Examples:
    # url(r'^$', 'singstreet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/',create_song),
    url(r'^view/',view_song),
    url(r'^delete/',delete_song),
#    url(r'^update/',update_song),
]
