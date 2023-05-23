from django.contrib import admin

from .models import Review

#customizar admin en la página de django
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id','user','movie', 'content']
    

# Register your models here.
admin.site.register(Review, ReviewAdmin)