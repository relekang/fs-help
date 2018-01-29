import httplib
import json
import string
import urllib
from random import choice

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

from fs_help.core.util import parse_name
from fs_help.lfs_help.models import UserGroup


def generate_password(length=8, chars=string.letters + string.digits):
    pw = ''.join([choice(chars) for i in range(length)])
    return pw


def login_with_lfs(username, password):
    url = settings.LFS_URL
    path = '/web/remote-auth.r'
    params = urllib.urlencode({
        'username': username,
        'password': password,
        'token': settings.LFS_TOKEN
    })
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    connection = httplib.HTTPConnection(url)
    connection.request("POST", path, params, headers)
    response = connection.getresponse().read()
    response = response.replace('<!-- Generated by Webspeed: http://www.webspeed.com/ -->',
                                '').strip()
    response = response.replace('\xe4', 'a').replace('\xf6', 'o')
    user_info = json.loads(response)['user']
    return user_info


def login(username, password):
    print "Login with lfs"
    debug = settings.DEBUG
    url = settings.LFS_URL
    print settings.DEBUG and settings.LFS_URL is None
    if settings.DEBUG and settings.LFS_URL is None:
        if username != "test" or password != "test":
            return None
        user_info = {"auth": True, "username": username, "language": "en", "name": "Test"}
    else:
        user_info = login_with_lfs(username, password)

    if not bool(user_info['auth']):
        return None

    try:
        user = User.objects.get(username=username)
    except (TypeError, User.DoesNotExist):
        user = User(username=username)
        user.save()
        profile = user.profile
        profile.language = user_info['language'].lower()
        try:
            group = UserGroup.objects.get(code=user_info['user_group'])
            profile.user_group = group
        except (TypeError, User.DoesNotExist):
            pass
        profile.save()
        user.is_active = True

    pw = generate_password()
    user.set_password(pw)
    name = parse_name(user_info['name'])
    user.first_name = name['first']
    user.last_name = name['last']
    user.save()
    user = authenticate(username=user.username, password=pw)
    return user


def login_view(request):
    if request.user.is_authenticated():
        if request.user.has_perm('lfs_help.change_topic'):
            return redirect(reverse('admin_topics'))
        else:
            return redirect(reverse('topics'))

    form = AuthenticationForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = login(username, password)
        if user is not None:
            if user.is_active:
                django_login(request, user)
                if user.has_perm('lfs_help.change_topic'):
                    return redirect(reverse('admin_topics'))
                else:
                    return redirect(reverse('topics'))

            else:
                messages.error(request, 'User is not active.')
        else:
            messages.error(request, 'Username or password was wrong')
    return render(request, 'registration/login.html', {'form': form})
