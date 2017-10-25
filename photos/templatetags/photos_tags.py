from django import template


register = template.Library()


@register.inclusion_tag('photos/tags/album_list.html',
                        takes_context=True)
def album_list(context, object_list, next_pages=None, category=None,
               collection=None, objects_number=None, model_name=None):
    """It's a part of the homepage and my albums views."""
    data = {'album_list': object_list,
            'request': context['request']}
    return data
