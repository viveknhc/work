from dataclasses import fields
from pyexpat import model
from .models import Apiusers
from rest_framework import serializers

class ApiUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Apiusers
        fields='__all__'