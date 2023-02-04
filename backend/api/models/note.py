from django.db import models

from api.models.base_model import BaseModel


class Note(BaseModel):
    user = models.ForeignKey("auth.User", related_name="notes", on_delete=models.CASCADE)
    content = models.TextField()
    x_loc = models.FloatField()
    y_loc = models.FloatField()
