from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    # Examples:
    # url(r'^$', 'singstreet.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^artist/', include('artist.urls')),
    url(r'^song/',include('song.urls')),
    url(r'^album/', include('album.urls')),
    url(r'^playlist/', include('album.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'', include('social_auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
