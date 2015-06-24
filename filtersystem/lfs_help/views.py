from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import activate

from filtersystem.core.shortcuts import render
from filtersystem.core.util import get_query
from filtersystem.lfs_help.models import Language, Topic


# @cache_page(604800)
def topic(request, slug, lang):
    lang = lang.lower()
    activate(lang)
    wrong_lang = False
    try:
        language = Language.objects.get(code=lang)
    except (KeyError, Language.DoesNotExist):
        language = Language.objects.get(code="no")
        wrong_lang = True
    try:
        topic = Topic.objects.get(slug=slug, language=language)
    except (KeyError, Topic.DoesNotExist):
        language = Language.objects.get(code="no")
        topic = get_object_or_404(Topic, slug=slug, language=language)
        wrong_lang = True
    if topic.need_auth and not request.user.is_authenticated() or topic.active is False:
        raise Http404
    return render(request, 'lfs_help/topic.html', {'topic': topic, 'wrong_language': wrong_lang})


@login_required
def list_topics(request):
    language = Language.objects.get(code=request.user.profile.language)
    topics = list(
        Topic.objects.filter(language=language, user_groups=request.user.profile.user_group,
                             active=True, parent=None).order_by('title'))
    topics += list(Topic.objects.filter(language=language, user_groups=None, active=True,
                                        parent=None).order_by('title'))
    topics.sort(key=lambda s: s.title)
    return render(request, 'lfs_help/list.html', {'topics': topics})


@login_required
def search(request):
    query = request.GET['query']
    q = get_query(query, ['title', 'content'], user=request.user)
    language = Language.objects.get(code=request.user.profile.language)
    topics = list(Topic.objects.filter(language=language,
                                       user_groups__contains=request.user.profile.user_group,
                                       active=True).filter(q))
    topics += list(Topic.objects.filter(language=language, user_groups=None, active=True).filter(q))
    topics.sort(key=lambda s: s.title)
    return render(request, 'lfs_help/search.html', {'topics': topics, 'query': query})


def redirect_mobile(request, next):
    url = 'http://www.lekang.com/wsScripts/cgiip.exe/WService=wslfshtml/m-login.r?neste=m-' + \
          next + '.r'
    return HttpResponseRedirect(url)
