from django.db import models

class User(models.Model):
    user_type_choices=(
        (1,'simple'),
        (2,'vip'),
        (3,'svip'),
    )
    user=models.CharField(max_length=32,unique=True)
    pwd=models.CharField(max_length=64)
    user_type=models.IntegerField(choices=user_type_choices)

class UserToken(models.Model):
    user=models.OneToOneField(to=User,on_delete=models.CASCADE)
    token=models.CharField(max_length=64)