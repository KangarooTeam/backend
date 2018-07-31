from django.db import models
from django.utils import timezone
from django import forms
from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey
import mptt

class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name="Родительский класс")
    class Meta():
        ordering = ('tree_id', "level")
        verbose_name_plural = "Категории"
        verbose_name = "Категории"

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/category_id/{}/".format(self.id)

mptt.register(Genre, order_insertion_by=['name'])

class Articles(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField()
    author = models.CharField(max_length=100, verbose_name="Автор", null=True, blank=True)
    tags = TaggableManager()
    category = TreeForeignKey(Genre, blank=True, null=True, related_name="cat")
    image = models.ImageField(
        blank=True, upload_to='images',
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
