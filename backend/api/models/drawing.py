from django.db import models

from api.models.base_models import BaseComponent


class Drawing(BaseComponent):
    content = models.BinaryField()
