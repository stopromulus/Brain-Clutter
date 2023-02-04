from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api.models import Note
from api.serializers import NoteSerializer



class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    @action(detail=True, methods=["GET"])
    def summarize(self, request, pk):
        note: Note = self.get_object()

        response = tell_gpt3(f'summarize {note.content}')

        return Response(data=response)
