# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserForm(forms.ModelForm):
    #    language = forms.CharField(max_length=6,widget=forms.Select(choices=settings.LANGUAGES))
    #    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'groups')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['is_active'].help_text = ''
        self.fields['groups'].widget.attrs['class'] = 'chosen'
        self.fields['groups'].help_text = _('Chose the what rights this user should have')
        self.fields['groups'].label = _('Permissons')

        if self.instance and self.instance.pk:
            self.fields['username'].widget.attrs['readonly'] = True
            self.fields['username'].help_text = ''
        #            self.fields['password'].widget = forms.HiddenInput()

        else:
            self.fields['is_active'].widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=commit)
        #        user.profile.set_language(self.cleaned_data['language'])
        #        user.set_password(self.cleaned_data['password'])
        user.is_active = True
        user.save()
