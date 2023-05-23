from django.contrib import admin
from .models import Movie
#customizar admin en la página de django
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'year']
    list_filter = ['year']

# Register your models here.
admin.site.register(Movie, MovieAdmin)