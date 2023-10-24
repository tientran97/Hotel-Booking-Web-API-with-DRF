from rest_framework import viewsets
from core.authentication.serializers import RegisterSerializer, UserSerializer
from core.authentication.utils import User, CreateOnlyModelViewSet


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-pk')
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-pk')
    serializer_class = UserSerializer
