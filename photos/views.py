from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from .models import Album


class HomepageView(ListView):
    template_name = 'photos/homepage.html'
    model = Album

    def get_queryset(self):
        q = super().get_queryset()
        return q.filter(is_public=True)
