from django import template
from ..models import Task

register = template.Library()

@register.simple_tag(takes_context=True)
def total_tasks(context):
    request = context['request']
    user = request.user
    task_count = Task.objects.filter(user=user).count()
    return task_count
