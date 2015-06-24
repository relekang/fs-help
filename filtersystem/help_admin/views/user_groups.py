from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.forms.models import modelformset_factory
from django.utils.translation import ugettext_lazy as _

from filtersystem.core.shortcuts import render
from filtersystem.lfs_help.models import UserGroup


@permission_required('lfs_help.can_change_usergroup')
def edit_user_groups(request):
    groups = UserGroup.objects.all()
    UserGroupFormSet = modelformset_factory(UserGroup, extra=0)
    formset = UserGroupFormSet(queryset=groups)
    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                form.save()
                messages.info(request, _('User groups saved'))

    return render(request, 'help_admin/user_groups/edit.html', locals())
