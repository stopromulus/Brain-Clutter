from rest_framework import serializers
from api.models import User, Note, Drawing

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email"]
class NoteSerializer(serializers.Serializer):
    class Meta:
        model = Note
        fields = ["user", "content", "x_loc", "y_loc"]

class DrawingSerializer(serializers.Serializer):
    class Meta:
        model = Drawing
        fields = ["user", "content", "x_loc", "y_loc"]