from django.conf.urls import url

from album.views import create_album,view_album,delete_album

urlpatterns = [
    # Examples:
    # url(r'^$', 'singstreet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/',create_album),
    url(r'^view/',view_album),
    url(r'^delete/',delete_album),
#    url(r'^update/',update_song),
]
