from rest_framework import serializers

from api.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        read_only_fields = ["user"]
        fields = read_only_fields + ["content", "x_loc", "y_loc"]
