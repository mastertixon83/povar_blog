from django.contrib import admin
from .models import *


class ImagesAboutInline(admin.StackedInline):
    model = ImageAbout
    extra = 1

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    save_as_continue = True

    list_display = ['pk', 'name', 'email', 'created_at']
    list_display_links = ['pk', 'name']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    save_as_continue = True

    list_display = ['pk', 'name']
    list_display_links = ['pk', 'name']

    inlines = [ImagesAboutInline]




admin.site.register(ContactLink)
admin.site.register(Social)