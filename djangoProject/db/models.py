from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
class CONF_PATH(models.Model):
    path = models.CharField(max_length=500)
    file = models.CharField(max_length=255,null=True)
