from django.contrib import admin
from .models import Post, another

# Register your models here.
admin.site.register(another)
admin.site.register(another.test)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        jsc = ('tinyInject.js',)
