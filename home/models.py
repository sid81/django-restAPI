
from django.db import models
import uuid
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100,default="default")
    completed=models.BooleanField(default=False,blank=True,null=True)
    
    def __str__(self):
        return self.title
    






