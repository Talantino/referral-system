from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from users.serializers import UserRegisterSerializer


class UserRegister(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
