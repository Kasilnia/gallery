from django.db import models

from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


# TODO change or delete UserProfile model
class UserProfile(User):
    email = models.EmailField(
        unique=True,
        error_messages={'unique': _('A user with that email already exists.')}
    ),

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return '{} {}'.format(self.username, self.email)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
