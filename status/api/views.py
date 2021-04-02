from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from rest_framework.generics import ListAPIView 

from rest_framework.authentication import SessionAuthentication

from status.models import Status
from .serializers import StatusSerializer

from django.shortcuts import get_object_or_404
import json

def is_json(json_data):
    try:
        real_json = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid


'''
CreateModelMixin  ----  POST method
RetrieveModelMixin  ----  GET method
UpdateModelMixin  ----  PUT method
DestroyModelMixin  ----  DELETE method
'''
class StatusAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # def perform_update(self, serializer):
    #     serializer.save(updated_by_user=self.request.user)
    
    # def perform_destroy(self, instance):
    #     if instance is not None:
    #         return instance.delete()
    #     return None


# Login required mixin / decorator

class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Is this person authenticated or not. Also can see the list
    # # permission_classes = [permissions.IsAuthenticated]  # Is this person authenticated or not.
    # authentication_classes = [SessionAuthentication]  # How they can be authenticted. Oauth, JWT
    serializer_class = StatusSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        # print(request.user)
        qs = Status.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




##### One End-Point Start #####
# class StatusAPIView(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer
#     passed_id = None

#     ## Override methods Start
#     def get_queryset(self):
#         request = self.request
#         qs = Status.objects.all()
#         query = request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def get_object(self):
#         request = self.request
#         passed_id = request.GET.get('id', None) or self.passed_id  # Because we didn't pass any id through path in urls.
#         queryset = self.get_queryset()
#         obj = None
#         if passed_id is not None:
#             obj = get_object_or_404(queryset, id=passed_id)
#             self.check_object_permissions(request, obj)  # DRF built in method - check_object_permissions
#         return obj

#     def perform_destroy(self, instance):
#         if instance is not None:
#             return instance.delete()
#         return None
#     ## Override methods End

#     def get(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get('id', None)
#         # print(request.body)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         if passed_id is not None:# or passed_id is not ''
#             return self.retrieve(request, *args, **kwargs)   # retrieve() is a default method comes with RetrieveModelMixin
#         return super().get(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get('id', None)
#         # print(request.body)
#         # print(request.data)
#         requested_id = request.data.get('id')
#         passed_id = url_passed_id or new_passed_id or requested_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get('id', None)
#         # print(request.body)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         url_passed_id = request.GET.get('id', None)
#         json_data = {}
#         body_ = request.body
#         if is_json(body_):
#             json_data = json.loads(request.body)
#         new_passed_id = json_data.get('id', None)
#         # print(request.body)
#         passed_id = url_passed_id or new_passed_id or None
#         self.passed_id = passed_id
#         return self.destroy(request, *args, **kwargs)
##### One End-Point End #####



# class StatusListSearchAPIView(APIView):
#     permission_classes = []
#     authentication_classes = []

#     def get(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         qs = Status.objects.all()
#         serializer = StatusSerializer(qs, many=True)
#         return Response(serializer.data)


# class StatusAPIView(generics.ListAPIView):
# class StatusAPIView(ListAPIView):
#     permission_classes = []
#     authentication_classes = []
#     # queryset = Status.objects.all()
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs


'''
CreateModelMixin  ----  POST method
UpdateModelMixin  ----  PUT method
DestroyModelMixin  ----  DELETE method
'''
# class StatusAPIView(mixins.CreateModelMixin, generics.ListAPIView):  # Create List
#     permission_classes = []
#     authentication_classes = []
#     serializer_class = StatusSerializer

#     def get_queryset(self):
#         qs = Status.objects.all()
#         query = self.request.GET.get('q')
#         if query is not None:
#             qs = qs.filter(content__icontains=query)
#         return qs

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#     # def perform_create(self, serializer):
#     #     serializer.save(user=self.request.user)  # Pass an argument whatever i want.




# class StatusCreateAPIView(generics.CreateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)  # Pass an argument whatever i want.





# class StatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'  # 'slug'

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)







# class StatusDetailAPIView(generics.RetrieveAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     # lookup_field = 'id'  # 'slug'

#     def get_object(self, *args, **kwargs):
#         kwargs = self.kwargs
#         kw_id = kwargs.get('id')  # 'id' from urls.py. We will give here what I gave in urls.
#         return Status.objects.get(id=kw_id)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'


# class StatusDeleteAPIView(generics.DestroyAPIView):
#     permission_classes = []
#     authentication_classes = []
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = 'id'








# class StatusCreateView(CreateView):
#     queryset = Status.objects.all()
#     form_class = StatusForm



