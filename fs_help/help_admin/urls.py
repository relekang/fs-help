from django.conf.urls import patterns, url

urlpatterns = patterns(
    'fs_help.help_admin.views',
    (r'^$', 'topics.landing_page'),
)

urlpatterns += patterns(
    'fs_help.help_admin.views.topics',
    url(r'^topics/$', 'landing_page', name='admin_topics'),
    url(r'^topics/(?P<id>\d+)/edit/$', 'edit_topic', name='edit_topic'),
    url(r'^topics/add/$', 'edit_topic', name='add_topic'),
    (r'^topics/(?P<slug>.*)/add-translation/$', 'add_translation'),
)

urlpatterns += patterns(
    'fs_help.help_admin.views.user_groups',
    url(r'^user-groups/$', 'edit_user_groups', name='admin_user_groups'),
)
