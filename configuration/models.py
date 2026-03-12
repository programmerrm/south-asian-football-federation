from django.db import models
from django.utils.translation import gettext_lazy as _

# LOGO
class Logo(models.Model):
    image = models.FileField(
        upload_to='logo/',
        verbose_name=_('Logo')
    )
    alt = models.CharField(
        max_length=280,
        null=True,
        blank=True,
        verbose_name=_('Logo Alt'),
    )
    width = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Width'),
    )
    height = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Height'),
    )

    class Meta:
        verbose_name = _("Logo")
        verbose_name_plural = _("Logo")
        ordering = ["-id"]

    def __str__(self):
        return self.alt if self.alt else "Logo {}".format(self.id)

# FAVICON
class Favicon(models.Model):
    favicon_ico = models.FileField(
        upload_to='favicon/',
        null=True,
        blank=True,
        verbose_name=_('Favicon ICO (.ico)'),
        help_text=_('Recommended size: 16x16, 32x32 (ICO format).'),
    )
    favicon_16 = models.FileField(
        upload_to='favicon/',
        null=True,
        blank=True,
        verbose_name=_('Favicon 16x16'),
        help_text=_('Recommended size: (16x16).'),
    )
    favicon_16_width = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon 16 Width'),
    )
    favicon_16_height = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon 16 Height'),
    )
    favicon_32 = models.FileField(
        upload_to='favicon/',
        null=True,
        blank=True,
        verbose_name=_('Favicon 32x32'),
        help_text=_('Recommended size: (32x32).'),
    )
    favicon_32_width = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon 32 Width'),
    )
    favicon_32_height = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon 32 Height'),
    )
    apple_touch_icon = models.FileField(
        upload_to='favicon/',
        null=True,
        blank=True,
        verbose_name=_('Apple Touch Icon (180x180)'),
        help_text=_('Recommended apple touch icon size: (180x180).'),
    )
    apple_width = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon Apple 32 Width'),
    )
    apple_height = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon Apple 180 Height'),
    )
    android_192 = models.FileField(
        upload_to='favicon/',
        null=True,
        blank=True,
        verbose_name=_('Android 192x192'),
        help_text=_('Recommended android icon size: (192x192).'),
    )
    android_192_width = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon ApAndroidple 192 Width'),
    )
    android_192_height = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon Android 192 Height'),
    )
    android_512 = models.FileField(
        upload_to='favicon/',
        null=True,
        blank=True,
        verbose_name=_('Android 512x512 (PWA)'),
        help_text=_('Recommended android icon size: (512x512) (PWA).'),
    )
    android_512_width = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon Android 512 Width'),
    )
    android_512_height = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon Android 512 Height'),
    )
    ms_tile_icon = models.FileField(
        upload_to='favicon/',
        null=True,
        blank=True,
        verbose_name=_('Microsoft Tile (144x144)'),
        help_text=_('Recommended microsoft icon size: (144x144).'),
    )
    ms_width = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon Microsoft 144 Height'),
    )
    ms_height = models.IntegerField(
        null=True, 
        blank=True,
        verbose_name=_('Favicon Microsoft 144 Height'),
    )

    class Meta:
        verbose_name = _("Favicon")
        verbose_name_plural = _("Favicon")
        ordering = ["-id"]

    def __str__(self):
        return f"Favicon ".format(self.id)
