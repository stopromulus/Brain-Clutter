from django.contrib import admin
from .models import BaseModel, User, Note, Drawing

# Register your models here.
admin.site.register(User)
admin.site.register(Note)
admin.site.register(Drawing)