from django.db import models

# Create your models here.

class Accounts(models.Model):
    username = models.CharField(default='username', max_length=20)
    identify = models.CharField(default='identify', max_length=20, unique=True, primary_key=True)
    password = models.CharField(default='password', max_length=20)