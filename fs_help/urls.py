from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse
from django.views.generic import RedirectView

admin.autodiscover()

urlpatterns = [
    url(
        r'^robots\.txt$',
        lambda r: HttpResponse("User-agent: *\nDisallow: /", content_type="text/plain")
    ),
    url(r'^admin/users/', include('fs_help.users.urls')),
    url(r'^admin/', include('fs_help.help_admin.urls')),
    url(r'^profile/', include('fs_help.core.profiles.urls')),
    url(r'^accounts/login/$', 'fs_help.core.auth.login_view', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^nadmin/', include(admin.site.urls)),
    url(r'^mobil/(?P<next>.*)/', 'fs_help.lfs_help.views.redirect_mobile'),
    url(r'^search/$', 'fs_help.lfs_help.views.search', name='search'),
    url(r'^topics/', 'fs_help.lfs_help.views.list_topics', name='topics'),
    url(r'^(?P<lang>\w{2})/(?P<slug>.*)/', 'fs_help.lfs_help.views.topic', name='view_topic'),
]

if not settings.DEBUG:
    urlpatterns = [url(r'^$', RedirectView.as_view(url=settings.LFS_LOGIN_URL))] + urlpatterns
else:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
