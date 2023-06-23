from rest_framework import serializers
from .models import Todo
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Customize token payload if needed
        token['username'] = user.username
        return token

class MyTokenRefreshSerializer(TokenRefreshSerializer):
    pass

