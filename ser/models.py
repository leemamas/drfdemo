from django.db import models

# Create your models here.

class User(models.Model):

    user=models.CharField(max_length=32,unique=True)
    pwd=models.CharField(max_length=64)

class UserToken(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    token=models.CharField(max_length=64)

class Role(models.Model):
    user=models.ManyToManyField(to=User)
    title=models.CharField(max_length=32)