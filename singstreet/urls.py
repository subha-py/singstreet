from django.conf.urls import include, url
from django.contrib import admin
urlpatterns = [
    # Examples:
    # url(r'^$', 'singstreet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^artist/', include('artist.urls')),
    url(r'^song/',include('song.urls')),
    url(r'^album/', include('album.urls')),
    url(r'^playlist/', include('album.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
