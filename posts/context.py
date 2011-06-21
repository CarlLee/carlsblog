from posts import settings
from django.template import RequestContext

def blog_info_processor(request):
    ctx = {
           'BLOG_TITLE': settings.BLOG_TITLE,
           'BLOG_SLOGAN': settings.BLOG_SLOGAN,
    }
    return ctx

class BlogInfoContext(RequestContext):
    def __init__(self, request, dict=None, processors=None, current_app=None, use_l10n=None):
        if processors:
            processors.append(blog_info_processor)
            RequestContext.__init__(self, request, dict=dict, processors=processors, current_app=current_app, use_l10n=use_l10n)
        else:
            RequestContext.__init__(self, request, dict=dict, processors=[blog_info_processor], current_app=current_app, use_l10n=use_l10n)
