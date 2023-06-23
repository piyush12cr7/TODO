from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('todos/', TodoListCreateAPIView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo-detail'),
]