from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _

from image_cropping import ImageRatioField

from stdimage.models import StdImageField
from stdimage.utils import UploadToClassNameDir


class Album(models.Model):
    user = models.ForeignKey(
        User, related_name='albums', verbose_name=_('User'))
    name = models.CharField(_('Name'), max_length=200)
    description = models.TextField(_('Short description'), blank=True)
    is_public = models.BooleanField(
        _('Is public'),
        default=False,
        help_text=_('Public album is shown for all users.'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')
        ordering = ('name',)


class Photo(models.Model):
    album = models.ForeignKey(
        Album, related_name='photos', verbose_name=_('Album'))
    image = StdImageField(_('Image'), upload_to=UploadToClassNameDir())
    cropping = ImageRatioField(
        'image', '100x100', size_warning=True,
        verbose_name=_('Cropping of Photo'))

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')
