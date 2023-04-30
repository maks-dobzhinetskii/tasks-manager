from django import template
from tasks.models import Task


register = template.Library()


@register.simple_tag()
def get_all_draft_tasks():
    return Task.draft_true.all()
