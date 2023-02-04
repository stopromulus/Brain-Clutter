from rest_framework import serializers
from api.models import User, Note, Drawing

class UserSerializer(serializers.Serializer):
    fields = ["id", "first_name", "last_name", "email"]

class NoteSerializer(serializers.Serializer):
    fields = ["user", "content", "x_loc", "y_loc"]

class DrawingSerializer(serializers.Serializer):
    fields = ["user", "content", "x_loc", "y_loc"]