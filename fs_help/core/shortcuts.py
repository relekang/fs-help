from django.shortcuts import render_to_response
from django.template.context import RequestContext


def render(request, template, values={}, error=None, info=None, public=False, *args, **kwargs):
    values['error_message'] = error
    values['info_message'] = info
    if request.user.is_authenticated():
        values['base_template'] = 'base_adv_view.html'
    else:
        values['base_template'] = 'base.html'

    if request.user.is_authenticated():
        values['profile'] = request.user.profile

    return render_to_response(template, values, *args, context_instance=RequestContext(request),
                              **kwargs)
