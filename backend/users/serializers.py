import random
import string
from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'is_superuser']

    def create(self, validated_data):

        if validated_data['is_superuser']:
            user = User.objects.create_superuser(
                email=validated_data['email'],
                password=validated_data['password'],
            )
        else:
            user = User.objects.create_user(
                email=validated_data['email'],
                password=validated_data['password'],
            )
        return user
