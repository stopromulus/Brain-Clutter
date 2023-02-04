import uuid
from django.db import models
from django.contrib import auth

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    time_created = models.DateTimeField(auto_created=True, editable=False)
    class Meta:
        abstract=True

class User(auth.models.User):
    pass

class Note(BaseModel): 
    user = models.ForeignKey("User", related_name="notes", on_delete=models.CASCADE)
    content = models.TextField()
    x_loc = models.FloatField()
    y_loc = models.FloatField()


class Drawing(BaseModel):
    user = models.ForeignKey("User", related_name="drawings", on_delete=models.CASCADE)
    content = models.BinaryField()
    x_loc = models.FloatField()
    y_loc = models.FloatField()