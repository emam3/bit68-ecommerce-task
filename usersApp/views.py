from django.shortcuts import render
from rest_framework import viewsets
from usersApp.serializers import userSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from usersApp.models import User
from usersApp.permisions import updateUser

class registerUser(viewsets.ModelViewSet):
    serializer_class = userSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (updateUser,)


class loginUser(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'Name' : user.get_full_name(),
                "token": token.key,
                "email": user.email
            }
        )

    # def post(self,request):
