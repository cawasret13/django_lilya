from rest_framework import serializers
from models import UsersLylya


class SerialUser(serializers.Serializer):
    _id = serializers.CharField(max_length=25)
    firstname = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=1000)
    telephone = serializers.CharField(max_length=16)
    email = serializers.CharField(max_length=100)
    cart = serializers.TextField(null=True)
    orders = serializers.TextField(null=True)

    def Create(self, validated_data):
        return UsersLylya.objects.create(**validated_data)
