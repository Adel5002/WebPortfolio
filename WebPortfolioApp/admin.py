from django.contrib import admin
from .models import *

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_img')
    search_fields = ('title', 'descr')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(PortfolioStructure, PortfolioAdmin)
admin.site.register(Comment)