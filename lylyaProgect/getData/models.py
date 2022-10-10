from django.db import models


class Subcatigory(models.Model):
    _id = models.CharField(max_length=100)
    name = models.CharField(max_length=500)


class Products(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=1000)
    price = models.FloatField(null=True)
    idProduct = models.CharField(max_length=500, null=True)
    idCategory = models.CharField(max_length=500, null=True)
    name_subcategory = models.CharField(max_length=100, null=True)
    amounts = models.IntegerField(null=True)
    idV = models.CharField(max_length=500, null=True)


class CategorysProduct(models.Model):
    id_category = models.CharField(max_length=500, null=True)
    name_category = models.CharField(max_length=500, null=True)
    name_subcategory = models.CharField(max_length=1000, null=True)
    id_subcategory = models.CharField(max_length=500, null=True)
    count_products_in_category = models.IntegerField(null=True)
