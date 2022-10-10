from rest_framework.response import Response
from rest_framework.views import APIView
from usersLylya.serialzer import SerialUser


class RegistrationUser(APIView):
    def post(self, request):
        serializer = SerialUser(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return  Response({'post': serializer.data})
