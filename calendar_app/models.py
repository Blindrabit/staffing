from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=200, default='free')
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return self.title + " - " + str(self.start_time) + " - " + str(self.end_time)