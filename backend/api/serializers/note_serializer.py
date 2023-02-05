from rest_framework import serializers

from api.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ["id"]
        fields = read_only_fields + ["content", "x", "y", "width", "height"]
