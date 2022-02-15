from django import template
from base.utils import get_object_or_none


register = template.Library()

@register.inclusion_tag('object_list.html')
def object_list(qset):
    context = {'qset': qset}
    return context
