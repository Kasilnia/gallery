from django.conf.urls import url

from .views import CustomSignupView, CustomLoginView, logout_user


urlpatterns = [
    url(r'^signup/$', CustomSignupView.as_view(), name='signup'),
    url(r'^login/$', CustomLoginView.as_view(), name='login'),
    url(r'^logout/$', logout_user, name='logout'),
]
