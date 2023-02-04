from rest_framework import viewsets

from api.models import Drawing
from api.serializers import DrawingSerializer


class DrawingViewSet(viewsets.ModelViewSet):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer
