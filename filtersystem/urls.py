from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    url(
        r'^robots\.txt$',
        lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")
    ),
    url(r'^admin/users/', include('filtersystem.users.urls')),
    url(r'^admin/', include('filtersystem.help_admin.urls')),
    url(r'^profile/', include('filtersystem.core.profiles.urls')),
    url(r'^accounts/login/$', 'filtersystem.core.auth.login_view', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^nadmin/', include(admin.site.urls)),
    url(r'^mobil/(?P<next>.*)/', 'filtersystem.lfs_help.views.redirect_mobile'),
    url(r'^search/$', 'filtersystem.lfs_help.views.search', name='search'),
    url(r'^topics/', 'filtersystem.lfs_help.views.list_topics', name='topics'),
    url(r'^(?P<lang>\w{2})/(?P<slug>.*)/', 'filtersystem.lfs_help.views.topic', name='view_topic'),
]

if not settings.DEBUG:
    urlpatterns = [url(r'^$', RedirectView.as_view(url=settings.LFS_LOGIN_URL))] + urlpatterns
else:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
