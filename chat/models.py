from django.db import models
from django.db.models.fields.json import JSONField

class Room(models.Model):
  name = models.CharField(max_length=100)
  messages = JSONField(blank=True, default=list)