from django.contrib import admin
from .models import Articles, Genre


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'image_img',)

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', "parent"]

admin.site.register(Articles, ImageAdmin)
admin.site.register(Genre, CategoryAdmin)