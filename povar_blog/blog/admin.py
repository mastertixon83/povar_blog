from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 1


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    """Регистрация модели категорий"""
    save_as = True
    save_on_top = True
    save_as_continue = True

    mptt_level_indent = 10
    list_display = ['pk', 'name', 'slug']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Регистрация модели тегов"""
    save_as = True
    save_on_top = True
    save_as_continue = True

    list_display = ['pk', 'name', 'slug']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name',), }


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Регистрация модели постов"""
    save_as = True
    save_on_top = True
    save_as_continue = True

    list_display = ['pk', 'title', 'category', 'created_at', 'author']
    list_display_links = ['title']
    inlines = [RecipeInline]
    prepopulated_fields = {'slug': ('title',), }


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Регистрация модели рецептов"""
    save_as = True
    save_on_top = True
    save_as_continue = True

    list_display = ['pk', 'name', 'prep_time', 'cook_time', 'post']
    list_display_links = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Регистрация модели комментариев"""
    save_as = True
    save_on_top = True
    save_as_continue = True

    list_display = ['pk', 'name', 'email']
    list_display_links = ['name']
