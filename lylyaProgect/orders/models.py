from django.db import models

class Orders(models.Model):
    _id_orders = models.IntegerField(null=True)
    delivery = models.BooleanField()
    _id_user = models.CharField(max_length=25)
    products = models.TextField()
    _id_courier = models.CharField(max_length=25, null=True)