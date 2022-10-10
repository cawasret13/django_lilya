from rest_framework.serializers import ModelSerializer
from getData.models import Products, CategorysProduct, Subcatigory


class SerializerProduct(ModelSerializer):
    class Meta:
        model = Products
        fields = ['name', 'price', 'image', 'idProduct', 'idCategory', 'name_subcategory', 'amounts']


class SerializerCategory(ModelSerializer):
    class Meta:
        model = CategorysProduct
        fields = ['name_category', 'id_category', 'name_subcategory', 'id_subcategory']

class SerializerSUBCategory(ModelSerializer):
    class Meta:
        model = Subcatigory
        fields = ['_id', 'name']
