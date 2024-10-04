from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TaskAPIView.as_view(), name='task-list'),
    path('tasks/<str:pk>/', TaskDetailView.as_view(), name='task-detail')
]