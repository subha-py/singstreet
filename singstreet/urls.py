from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'singstreet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    #user created urls
    url(r'^artist/', include('artist.urls',namespace='artist')),
    url(r'^song/',include('song.urls',namespace='song')),
    url(r'^album/', include('album.urls',namespace='album')),
    #url(r'^playlist/', include('album.urls'),namespace='playlist'),
    #admin page urls
    url(r'^admin/', include(admin.site.urls)),
    #main page url
    url(r'^$',TemplateView.as_view(template_name='home.html'), name='home'),
    #thrid party urls
    url(r'^accounts/', include('allauth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#django_debug_urls
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     ]