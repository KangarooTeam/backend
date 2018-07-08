from django.contrib import admin
from .models import Articles, TopArticles


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'image_img',)



admin.site.register(Articles, ImageAdmin)

admin.site.register(TopArticles)
