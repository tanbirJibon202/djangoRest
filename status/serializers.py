from rest_framework import serializers
from status.models import Status
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class StatusSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False)
    class Meta:
        model = Status
        fields = ['id', 'text', 'created_at', 'user']
