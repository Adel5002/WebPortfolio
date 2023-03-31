from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'upload_img')
#     search_fields = ('title', 'descr')
#     list_display_links = ('id', 'title')
#     prepopulated_fields = {'slug': ('title',)}


class PortfolioTrans(TranslationAdmin):
    model = PortfolioStructure


admin.site.register(PortfolioStructure, PortfolioTrans)
admin.site.register(Comment)

