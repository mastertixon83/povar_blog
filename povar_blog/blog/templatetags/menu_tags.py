from django import template
from blog.models import *

register = template.Library()


def get_all_categories():
    return Category.objects.all()


@register.simple_tag()
def get_list_category():
    return get_all_categories()


@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    # .filter(parent__isnull=True)
    category = get_all_categories()#order_by('name')
    return {'list_category': category}


@register.inclusion_tag('blog/include/tags/recepts_tag.html')
def get_last_posts():
    # .filter(parent__isnull=True)
    posts = Post.objects.select_related('category').order_by('-pk')[:5]#order_by('name')
    return {'list_last_post': posts}