from rest_framework import serializers
from django import forms

from .models import Users, Profile, Products, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        widgets = {
            "password": forms.PasswordInput()
        }
