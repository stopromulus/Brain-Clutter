from django.db import models

from api.models.base_model import BaseModel


class Drawing(BaseModel):
    user = models.ForeignKey("auth.User", related_name="drawings", on_delete=models.CASCADE)
    content = models.BinaryField()
    x_loc = models.FloatField()
    y_loc = models.FloatField()
