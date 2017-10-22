from django.conf.urls import url

from photos.views import homepage


urlpatterns = [
    url(r'', homepage, name='homepage'),
]
