from django.conf import settings
from django.contrib import admin

from fs_help.lfs_help.models import Language, Topic, UserGroup

media = settings.MEDIA_URL

js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
      media + '/js/wymeditor/jquery.wymeditor.js', media + '/js/editor.js')


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')


admin.site.register(Language, LanguageAdmin)


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')


admin.site.register(UserGroup, UserGroupAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'active', 'parent', 'order')
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'active', 'language', 'order')
        }),
        ('Avansert', {
            'classes': ('collapse',),
            'fields': ('need_auth', 'parent', 'user_groups')
        }),
    )
    list_filter = ('active', 'need_auth', 'language', 'user_groups')

    def save_model(self, request, obj, form, change):
        obj.saved_by = request.user
        obj.save()

    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/1.3.2/jquery.min.js',
              media + '/js/wymeditor/jquery.wymeditor.js', media + '/js/fancyedit.js')


admin.site.register(Topic, TopicAdmin)


# class ImageAdmin(admin.ModelAdmin):
#    list_display = ('title', 'description','saved_by')
#    fieldsets = (
#        (None, {
#            'fields': ('title', 'description', 'file', 'language')
#        }),
#    )
#    def save_model(self, request, obj, form, change):
#        obj.saved_by = request.user
#        obj.save()
#
# admin.site.register(Image, ImageAdmin)
