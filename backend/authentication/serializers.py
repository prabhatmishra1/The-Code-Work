from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model  # If used custom user model
from . models import *
UserModel = get_user_model()


class LoginSerailizer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email', 'password']


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        fields = ("id", "email", "mobile", "password",)
