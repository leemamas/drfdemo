from django.db import models


class BaseModel(models.Model):
    is_detele = models.BooleanField(default=False)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class BookModel(models.Model):
    name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    publish=models.ForeignKey('PublishModel',on_delete=models.CASCADE)
    authors=models.ManyToManyField('AuthorModel')

class PublishModel(models.Model):
    name=models.CharField(max_length=32)
    address=models.CharField(max_length=64)

class AuthorModel(models.Model):
    name=models.CharField(max_length=32)
    age=models.IntegerField()

class AuthorDetailModel(models.Model):
    author=models.OneToOneField('AuthorModel',on_delete=models.DO_NOTHING)
    telphone=models.IntegerField(max_length=11)