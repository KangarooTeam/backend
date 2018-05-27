from django.db import models
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date = models.DateTimeField()
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