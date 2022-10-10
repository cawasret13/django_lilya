from django.db import models


class UsersLylya(models.Model):
    _id = models.CharField(max_length=25)
    firstname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1000)
    telephone = models.CharField(max_length=16)
    email = models.CharField(max_length=100)
    cart = models.TextField(null=True)
    orders = models.TextField(null=True)
