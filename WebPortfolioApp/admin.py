from django.contrib import admin
from .models import *

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'upload_img')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'descr')


admin.site.register(PortfolioStructure, PortfolioAdmin)