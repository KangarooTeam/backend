from django.db import models
from django.utils import timezone
from django import forms

class Articles(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100, verbose_name="Автор", null=True, blank=True)
    image = models.ImageField(
        blank=True, upload_to='images/%Y/%m/%d/',
        help_text='150x150px',
        verbose_name='Ссылка картинки'
    )

    def __str__(self):
        return self.title

    def image_img(self):
        if self.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url)
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def get_absolute_url(self):
        return "/post/%i/" % self.id

