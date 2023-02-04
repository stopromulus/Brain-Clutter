from django.shortcuts import render
from rest_framework import viewsets
from api.models import User, Drawing, Note
from api.serializers import UserSerializer, NoteSerializer, DrawingSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class DrawingViewSet(viewsets.ModelViewSet):
    queryset = Drawing.objects.all()
    serializer_class = DrawingSerializer