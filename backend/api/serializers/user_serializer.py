from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ["id"]
        fields = read_only_fields + ["first_name", "last_name", "email"]
