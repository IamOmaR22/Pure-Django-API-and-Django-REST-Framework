from django.urls import path, re_path
from .views import UpdateModelDetailAPIView, UpdateModelListAPIView

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),  # api/updates - List/Create
    path('<int:id>/', UpdateModelDetailAPIView.as_view()),  # <int:id>/ will take only digits.
    # re_path('(?P<id>\d+)/', UpdateModelDetailAPIView.as_view()),  # (?P<id>\d+) will take only digits.
]