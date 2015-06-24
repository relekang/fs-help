# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'filtersystem.users.views',
    url(r'^$', 'list_users', name='admin_users'),
    url(r'^add/$', 'edit_user', name='add_user'),
    url(r'^(?P<user_id>\d+)/edit/$', 'edit_user', name='edit_user'),
)
