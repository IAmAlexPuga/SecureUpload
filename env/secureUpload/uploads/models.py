from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=25)
    extension = models.CharField(max_length=6, default=".")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
