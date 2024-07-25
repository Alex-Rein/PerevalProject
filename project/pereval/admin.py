from django.contrib import admin
from .models import Pereval, User, Image, Level


class PerevalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'coord', 'user', 'status')
    list_filter = ('title', 'user', 'add_time')


# Register your models here.
admin.site.register(Pereval, PerevalAdmin)
admin.site.register(User)
admin.site.register(Image)
admin.site.register(Level)
