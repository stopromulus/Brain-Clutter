from django.db import models

from api.models.base_model import BaseModel


class Drawing(BaseModel):
    content = models.BinaryField()
    x_loc = models.FloatField()
    y_loc = models.FloatField()
