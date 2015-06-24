from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filtersystem.lfs_help.models import Language, UserGroup


class Profile(models.Model):
    user = models.ForeignKey(User, related_name='profile', unique=True, verbose_name=_('user'))
    user_group = models.ForeignKey(UserGroup, null=True, blank=True, verbose_name=_('user group'))
    language = models.CharField(max_length=6, default=settings.LANGUAGE_CODE,
                                choices=settings.LANGUAGES, verbose_name=_('language'))

    def __unicode__(self):
        return self.user.get_full_name()

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        cache.set('profile' + str(self.user.pk), self)

    def set_language(self, lang_code):
        try:
            self.language = Language.objects.get(code=lang_code)
            self.save()
        except (TypeError, Language.DoesNotExist):
            pass

    @classmethod
    def get_or_create(cls, user):
        profile = cache.get('profile' + str(user.pk))
        if not profile:
            try:
                profile = Profile.objects.get(user=user)
            except (TypeError, Profile.DoesNotExist):
                profile = Profile.objects.create(user=user)
                profile.save()
                cache.set('profile' + str(user.pk), profile, 604800)
        return profile

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')


User.profile = property(lambda u: Profile.get_or_create(user=u))
