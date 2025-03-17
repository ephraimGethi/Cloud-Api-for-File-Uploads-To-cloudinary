from django.contrib import admin
from .models import *
from django.utils.html import format_html 

@admin.register(computer)
class ComputerAdmin(admin.ModelAdmin):
    fields = ['name','avatar','video','document','description','updated_at','created_at','get_image_url']
    list_display = ['name','avatar','video','document','description','updated_at','created_at','get_image_url']
    readonly_fields = ['updated_at','created_at','get_image_url']
    search_fields = ["name","description"]
    ordering = ('-updated_at',)
    list_filter = ('updated_at', 'created_at')

    def get_image_url(self,obj):
        img_html = f'<img src="{obj.image_url()}" width="100" style="border-radius:17px 70px 30px 5px"/>'
        return format_html(img_html)
    
    get_image_url.short_description="eph img"