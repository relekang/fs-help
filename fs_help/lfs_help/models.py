# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from fs_help import core


class Language(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    code = models.CharField(max_length=2, verbose_name=_('code'),
                            help_text=_('Two lowercase letters. Ex: no for Norwegian'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')
        ordering = ["name"]


class UserGroup(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('name'))
    code = models.CharField(max_length=3, unique=True, verbose_name=_('code'))

    def __unicode__(self):
        return self.code.upper() + ': ' + self.name

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        super(UserGroup, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('user group')
        verbose_name_plural = _('user groups')
        ordering = ["code"]


class Topic(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True,
                               verbose_name=_('superior'))
    slug = models.CharField(max_length=100, verbose_name=_('code'),
                            help_text=_('www.filtersystem.no/no/[kode]'))
    content = models.TextField(verbose_name=_('content'))
    order = models.IntegerField(default=10, verbose_name=_('order'), help_text=_(
        'Sorting according to other documents with same superior'))
    need_auth = models.BooleanField(verbose_name=_('need authorisation'))
    active = models.BooleanField(verbose_name=_('active'))
    language = models.ForeignKey(Language, verbose_name=_('languages'))
    user_groups = models.ManyToManyField(
        UserGroup,
        verbose_name=_('user groups'),
        blank=True,
        null=True,
        help_text=_('Which user groups should have access to this document. If everyone should '
                    'have access do not select anyone.') + '\n'
    )
    saved_by = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.saved_by = core.get_current_user()
        super(Topic, self).save(*args, **kwargs)

    def available_languages(self):
        lang = ""
        for t in Topic.objects.filter(slug=self.slug):
            if t.language:
                if not lang == "":
                    lang += ", "
                lang += t.language.name
        return lang

    def lang_link_list(self):
        base_str = '<a href="%s">%s</a>'
        links = [
            base_str % (reverse('edit_topic', args=[translation.pk]), translation.language)
            for translation in self.translations()
            ]

        return mark_safe(', '.join(links))

    def translations(self):
        return Topic.objects.filter(slug=self.slug)

    class Meta:
        verbose_name = _('topic')
        verbose_name_plural = _('topics')
        unique_together = ('language', 'slug')
