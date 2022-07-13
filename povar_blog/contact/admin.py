from django.contrib import admin
from .models import *


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    save_as_continue = True

    list_display = ['pk', 'name', 'email', 'created_at']
    list_display_links = ['name']


admin.site.register(ContactLink)

