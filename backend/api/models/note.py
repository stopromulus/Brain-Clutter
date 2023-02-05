from django.db import models

from api.models.base_model import BaseModel


class Note(BaseModel):
    content = models.TextField()
    x_loc = models.FloatField()
    y_loc = models.FloatField()
