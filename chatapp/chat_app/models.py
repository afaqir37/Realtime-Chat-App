from django.db import models
from django.utils import timezone

class ChatRoom(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
            app_label = 'chatapp'

    def __str__(self):
        return self.name
    
class Message(models.Model):
    value = models.CharField(max_length=1000000, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now , blank = True)
    user = models.CharField(max_length=1000000, null=True, blank=True)
    room = models.CharField(max_length=1000000, null=True, blank=True)

    class Meta:
            app_label = 'chatapp'

    def __str__(self):
        return self.value