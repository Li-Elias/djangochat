from django.db import models
from django.utils import timezone

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    
class Message(models.Model):
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)
    user = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)