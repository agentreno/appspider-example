from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    max_participants = models.IntegerField()
