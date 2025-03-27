from django.contrib import admin
from .models import *
from django.utils.html import format_html 

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    fields = ['name','avatar','video','document','description','updated_at','created_at','get_image_url','get_document_url']
    list_display = ['name','avatar','video','document','description','updated_at','created_at','get_image_url','get_document_url']
    readonly_fields = ['updated_at','created_at','get_image_url','get_document_url']
    search_fields = ["name","description"]
    ordering = ('-updated_at',)
    list_filter = ('updated_at', 'created_at')

    def get_image_url(self,obj):
        img_html = f'<img src="{obj.image_url()}" width="100" style="border-radius:17px 70px 30px 5px"/>'
        return format_html(img_html)
    
    get_image_url.short_description="eph img"

    def get_document_url(self, obj):
        if obj.document:
            document_html = f'<a href="{obj.document.url}" target="_blank">View Document</a>'
            return format_html(document_html)
        return "No document uploaded"
    
    # def get_document_url(self, obj):
    #     if obj.document:
    #         document_url = obj.document.build_url(resource_type="raw", flags="attachment")
    #         print("Document URL:", document_url)  # Debugging: check URL
    #         return format_html(f'<a href="{document_url}" target="_blank" rel="noopener noreferrer">Download Document</a>')
    #     return "No document uploaded"

    get_document_url.short_description = "Document"
    #   hey