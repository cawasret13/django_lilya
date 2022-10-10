from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import SerializerOrder


class AddOrder(APIView):
    def post(self, request):
        review = SerializerOrder(data=request.data)
        print('hello')
        if (review.is_valid()):
            review.save()
        return Response({"body":request.data})

    @classmethod
    def get_extra_actions(cls):
        return []

