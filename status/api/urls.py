from django.urls import path

# from .views import StatusListSearchAPIView
from .views import StatusAPIView, StatusCreateAPIView, StatusDetailAPIView, StatusUpdateAPIView, StatusDeleteAPIView

urlpatterns = [
    # path('', StatusListSearchAPIView.as_view()),
    path('', StatusAPIView.as_view()),
    path('create/', StatusCreateAPIView.as_view()),
    path('<int:id>/', StatusDetailAPIView.as_view()),
    path('<int:id>/update/', StatusUpdateAPIView.as_view()),
    path('<int:id>/delete/', StatusDeleteAPIView.as_view()),
]


# Start With
# /api/status/  -->  List
# /api/status/create/  -->  Create
# /api/status/12/  -->  Detail
# /api/status/12/update/  -->  Update
# /api/status/12/delete/  -->  Delete


# End With
# /api/status/  -->  List  --> CRUD
# /api/status/1/  -->  Detail  --> CRUD


# Final
# /api/status/  -->  CRUD & LS (List and Search)
