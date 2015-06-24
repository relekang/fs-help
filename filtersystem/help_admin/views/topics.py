from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _

from filtersystem.core.shortcuts import render
from filtersystem.lfs_help.forms import TopicForm, TopicTranslationForm
from filtersystem.lfs_help.models import Topic


@permission_required('lfs_help.change_topic')
def landing_page(request):
    topics = cache.get('topicsno')
    if not topics:
        topics = Topic.objects.filter(language__code='no')
        cache.set('topicsno', topics)
    context = {'topics': topics}
    return render(request, 'help_admin/topics/base.html', context)


@permission_required('lfs_help.change_topic')
def edit_topic(request, id=None):
    form = TopicForm()
    if id is not None:
        instance = get_object_or_404(Topic, pk=id)
        form = TopicForm(instance=instance)

    if request.method == 'POST':
        form = TopicForm(request.POST)
        if id is not None:
            form = TopicForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.info(request, _('Topic was saved'))
            return redirect(reverse('admin_topics'))
    context = {'form': form,
               'title': _('Edit topic'),
               'tiny_mce': True}
    return render(request, 'help_admin/topics/form.html', context)


@permission_required('lfs_help.change_topic')
def add_translation(request, slug):
    base = Topic.objects.get(language__code='no', slug=slug)
    instance = Topic(title=base.title, slug=base.slug, order=base.order, need_auth=base.need_auth,
                     parent=base.parent)
    form = TopicTranslationForm(instance=instance)
    if request.method == 'POST':
        form = TopicTranslationForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.info(request, _('Topic was saved'))
            return redirect(reverse('admin_topics'))
    context = {'form': form,
               'title': _('Add translation'),
               'tiny_mce': True}
    return render(request, 'help_admin/topics/form.html', context)
