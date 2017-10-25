from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('auth_ex.urls', namespace='auth_ex')),
    url(r'^accounts/', include('allauth.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


urlpatterns += [
    url(r'', include('photos.urls', namespace='photos')),
]
