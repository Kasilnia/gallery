from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, FormView

from .forms import UploadForm
from .models import Album


class HomepageView(ListView):
    template_name = 'photos/homepage.html'
    model = Album

    def get_queryset(self):
        q = super().get_queryset()
        return q.filter(is_public=True)


class UploadView(FormView):
    template_name = 'photos/upload.html'
    form_class = UploadForm
    success_url = ''
