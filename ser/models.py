from django.db import models

# Create your models here.

class User(models.Model):
    user_type_choices = (
        (1, 'simple'),
        (2, 'vip'),
        (3, 'svip'),
    )
    user=models.CharField(max_length=32,unique=True)
    pwd=models.CharField(max_length=64)
    user_type=models.IntegerField(choices=user_type_choices)
    roles=models.ManyToManyField('Role')
    group=models.ForeignKey('UserGroup',on_delete=models.CASCADE)


class UserToken(models.Model):
    user=models.OneToOneField('User',on_delete=models.CASCADE)
    token=models.CharField(max_length=64)

class Role(models.Model):
    # users=models.ManyToManyField('User')
    title=models.CharField(max_length=32)

class UserGroup(models.Model):
    title=models.CharField(max_length=32)
