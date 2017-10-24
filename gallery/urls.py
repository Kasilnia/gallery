from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('auth_ex.urls', namespace='auth_ex')),
    url(r'^accounts/', include('allauth.urls')),
]


urlpatterns += [
    url(r'', include('photos.urls', namespace='photos')),
]
