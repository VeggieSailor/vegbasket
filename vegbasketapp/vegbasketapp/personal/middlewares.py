from django.contrib import messages

from social import exceptions as social_exceptions
from django.http import HttpResponseRedirect
from social.apps.django_app.middleware import SocialAuthExceptionMiddleware

class VSSocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    """Simply middleware redirecting to login page in case of an error.
    """
    def process_exception(self, request, exception):
        if hasattr(social_exceptions, exception.__class__.__name__):
            messages.add_message(request, messages.ERROR, exception)
            return HttpResponseRedirect('/login/')
        else:
            raise exception

