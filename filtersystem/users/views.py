# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _

from filtersystem.core.shortcuts import render
from filtersystem.users.forms import UserForm


@permission_required('auth.change_user')
def list_users(request):
    users = User.objects.all().order_by('username')
    return render(request, 'users/base.html', locals())


@permission_required('auth.change_user')
def edit_user(request, user_id=None):
    form = UserForm()
    title = _('Create new user')
    if user_id is not None:
        user = get_object_or_404(User, pk=user_id)
        title = _('Edit %(object)s' % {'object': user.username})
        form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST)
        if user_id is not None:
            form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        else:
            print form.errors

        print request.POST

    return render(request, 'users/edit_user.html', locals())
