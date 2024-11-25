from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=20)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    tg_id = models.CharField(max_length=20)

class Tasks(models.Model):
    
    title = models.CharField(max_length=20)
    description = models.TextField()
    status = models.BooleanField(default=False)
    deadline = models.DateTimeField()