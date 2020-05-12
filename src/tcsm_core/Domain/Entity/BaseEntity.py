from django.db import models
import uuid
from django.utils import timezone

class BaseModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(default=timezone.now)
    isDeleted = models.BooleanField(default=False)
    id = models.IntegerField(primary_key=True, editable=False)

    class Meta :
        abstract = True
