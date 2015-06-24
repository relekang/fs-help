from django.forms.models import ModelForm

from filtersystem.core.profiles.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'user_group')
