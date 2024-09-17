from django.urls import path
from .views import create_task #TaskListView, TaskDetailView

urlpatterns = [
    # path('tasks/', TaskListView.as_view(), name='task-list'),
    # path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/create/', create_task, name='task-create'),
]