import json  # json is a Python built in library.

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from pda_drf.mixins import JsonResponseMixin

from .models import Update

# def detail_view(request):
    # return render()  # return JSON data --> JS Object Notation
    # return HttpResponse(get_template().render({}))

# obj = Update.objects.get(id=1)

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

'''
class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        data = serialize("json", [obj, ], fields=('user', 'content'))
        # print(data)
        json_data = data
        # data = {
        #     'user': obj.user.username,
        #     'content': obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        # data = serialize("json", qs))  # qs is a list here. This line will serialize the data for me. All the fields are associated with the model.
        data = serialize("json", qs, fields=('user', 'content'))  # We want the field we set. Now we can serialized the data with fields which i declared.
        # $ python manage.py dumpdata --format json --indent 4  # You can see serialized data. Comes through by default using django's built in serializer.
        # $ python manage.py dumpdata updates.Update --format json --indent 4  # Specific App and Model. To see this, must need to some data in model.
        print(data)
        json_data = data
        # data = {
        #     'user': obj.user.username,
        #     'content': obj.content
        # }
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
'''

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = Update.objects.all().serialize()  # It will give us the serialize version of query set.
        return HttpResponse(json_data, content_type='application/json')