from django import template
from blog.models import *

register = template.Library()


# @register.simple_tag()

@register.inclusion_tag('blog/include/tags/top_menu.html')
def get_categories():
    # .filter(parent__isnull=True)
    category = Category.objects.all()#order_by('name')
    return {'list_category': category}


@register.inclusion_tag('blog/include/tags/recepts_tag.html')
def get_last_posts():
    # .filter(parent__isnull=True)
    posts = Post.objects.select_related('category').order_by('-pk')[:5]#order_by('name')
    return {'list_last_post': posts}