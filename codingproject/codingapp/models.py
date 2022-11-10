from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Khojsearch(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payload')
    inputlist = ArrayField(ArrayField(models.CharField(max_length=10, blank=True),size=20,),size=20,)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.user_id)
