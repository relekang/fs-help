from django.core.cache import cache
from fs_help.core.shortcuts import render
from fs_help.lfs_help.models import Topic


def landing_page(request):
    topics = cache.get('topics')
    if not topics:
        topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'help_admin/base.html', context)
