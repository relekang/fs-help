from django.core.cache import cache
from filtersystem.core.shortcuts import render
from filtersystem.lfs_help.models import Topic


def landing_page(request):
    topics = cache.get('topics')
    if not topics:
        topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'help_admin/base.html', context)
