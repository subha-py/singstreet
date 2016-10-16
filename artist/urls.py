from django.conf.urls import url

from artist.views import create_artist,view_artist,delete_artist,login_artist,signup_artist

urlpatterns = [
    # Examples:
    # url(r'^$', 'singstreet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^create/',create_artist),
    url(r'^signup/',signup_artist),
    url(r'^view/(?P<username>[\w-]+)/$', view_artist, name='view'),
    url(r'^delete/',delete_artist),
    url(r'^login/',login_artist),
#    url(r'^update/',update_song),
]
