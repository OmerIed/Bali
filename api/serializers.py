from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from main_app.models import *


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('username', 'email', 'password')

