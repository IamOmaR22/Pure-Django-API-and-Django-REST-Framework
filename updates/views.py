import json  # json is a Python built in library.
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from django.views.generic import View
from pda_drf.mixins import JsonResponseMixin

from .models import Update

# def detail_view(request):
    # return render()  # return JSON data --> JS Object Notation
    # return HttpResponse(get_template().render({}))


def json_example_view(request):
    '''
    URI (Uniform Resource Identifier) - for a REST Api
    GET - Request
    '''
    data = {
        'count': 1000,
        'content': 'Some new content'
    }
    json_data = json.dumps(data)
    # return JsonResponse(data)   # Python dictionary turns into a JSON dictionary with this shortcut.
    return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content'
        }
        return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            'count': 1000,
            'content': 'Some new content'
        }
        return self.render_to_json_response(data)

