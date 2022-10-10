from rest_framework.serializers import ModelSerializer

import orders


class SerializerOrder(ModelSerializer):
    class Meta:
        model = orders
        fields = 'delivery', '_id_user', 'products'
