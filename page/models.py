from django.db import models
from django.utils import timezone
from django import forms
from taggit.managers import TaggableManager

class Articles(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100, verbose_name="Автор", null=True, blank=True)
    tags = TaggableManager()
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


class TopArticles(models.Model):
    title_top = models.CharField(max_length=120)
    body_top = models.TextField()
    date_top = models.DateTimeField()
    author_top = models.CharField(max_length=100, verbose_name="Автор", null=True, blank=True)
    tags_top = TaggableManager()
    image_top = models.ImageField(
        blank=True, upload_to='images/%Y/%m/%d/',
        help_text='150x150px',
        verbose_name='Ссылка картинки'
    )

    def __str__(self):
        return self.title_top

    def image_img_top(self):
        if self.image_top:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image_top.url)
        else:
            return '(Нет изображения)'

    image_img_top.short_description = 'Картинка'
    image_img_top.allow_tags = True

    def get_absolute_url_top(self):
        return "/post_top/%i/" % self.id