from django.db import models


class Users(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    tg = models.CharField(max_length=20)

class Tasks(models.Model):
    tg= models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.TextField()
    status = models.BooleanField(default=False)
    deadline = models.DateTimeField()