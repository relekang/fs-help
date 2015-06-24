from django import forms
from django.template.base import Library
from django.utils.translation import ugettext_lazy as _

from filtersystem.lfs_help.models import Topic

register = Library()


@register.inclusion_tag('lfs_help/templatetags/sidebar_info.html', takes_context=True)
def sidebar_info(context, topic):
    user = context['user']
    related_topics = []
    related_topics += [t for t in
                       topic.children.filter(user_groups=user.profile.user_group, active=True)]
    related_topics += [t for t in topic.children.filter(user_groups=None, active=True)]
    if topic.parent is not None:
        related_topics = [topic.parent]
        related_topics += [t for t in
                           topic.parent.children.filter(user_groups=user.profile.user_group,
                                                        active=True).exclude(id=topic.id)]
        related_topics += [t for t in
                           topic.parent.children.filter(user_groups=None, active=True).exclude(
                               id=topic.id)]

    other_languages = Topic.objects.filter(slug=topic.slug).exclude(id=topic.id)

    return {
        'related_topics': related_topics,
        'other_languages': other_languages,
    }


class SearchForm(forms.Form):
    query = forms.CharField(label='')

    def __init__(self, query):
        super(SearchForm, self).__init__()
        self.fields['query'].initial = query
        self.fields['query'].widget.attrs['class'] = 'input-medium search-query'


@register.inclusion_tag('lfs_help/templatetags/search.html')
def search(query=None):
    form = SearchForm(query)
    return {
        'form': form
    }
