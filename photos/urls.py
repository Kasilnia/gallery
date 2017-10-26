from django.conf.urls import url

from photos.views import HomepageView, UploadView


urlpatterns = [
    url(r'^upload/$', UploadView.as_view(), name='upload'),
    url(r'', HomepageView.as_view(), name='homepage'),
]
