from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer, MyTokenObtainPairSerializer, MyTokenRefreshSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class MyTokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenRefreshSerializer
class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)

class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = (permissions.IsAuthenticated,)