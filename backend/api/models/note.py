from django.db import models

from api.models.base_models import BaseComponent


class Note(BaseComponent):
    content = models.TextField(blank=True)
    width = models.FloatField()
    height = models.FloatField()
