from rest_framework import serializers

from api.models import Drawing


class DrawingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drawing
        read_only_fields = ["user"]
        fields = read_only_fields + ["content", "x_loc", "y_loc"]
