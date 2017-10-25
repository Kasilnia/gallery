from django.conf.urls import url

from photos.views import HomepageView


urlpatterns = [
    url(r'', HomepageView.as_view(), name='homepage'),
]
