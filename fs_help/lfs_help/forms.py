from django import forms
from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _

from fs_help.lfs_help.models import Language, Topic


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        exclude = ('saved_by',)

    def __init__(self, *args, **kwargs):
        super(TopicForm, self).__init__(*args, **kwargs)
        self.fields['user_groups'].widget.attrs['class'] = 'chosen'
        self.fields['parent'].widget.attrs['class'] = 'chosen'
        self.fields['language'].widget.attrs['class'] = 'chosen'
        self.fields['user_groups'].help_text = self.fields['user_groups'].help_text.replace(
            'Hold down "Control", or "Command" on a Mac, to select more than one.', '')

        if self.instance and self.instance.pk:
            topics = Topic.objects.filter(language=self.instance.language).exclude(
                slug=self.instance.slug)
            self.fields['parent'].queryset = topics
        else:
            self.fields['active'].widget = forms.CheckboxInput(attrs={'checked': True})


class TopicTranslationForm(ModelForm):
    class Meta:
        model = Topic
        fields = ('title', 'language', 'content')

    def __init__(self, *args, **kwargs):
        super(TopicTranslationForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            languages = Language.objects.all()
            topics = Topic.objects.filter(slug=self.instance.slug)
            for t in topics:
                languages = languages.exclude(code=t.language.code)
            self.fields['language'].queryset = languages
            self.fields['language'].help_text = _(
                'If you cannot find your languages the file is already translated.')
            self.fields['user_groups'].widget.attrs['class'] = 'chosen'
            self.fields['language'].widget.attrs['class'] = 'chosen'
