from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)  # we can use this method decorator for all the methods in views
    def dispatch(self, *args, **kwargs):  # dispatch for get, post, put, delete.
        return super().dispatch(*args, **kwargs)  # super(CSRFExemptMixin, self)