from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser

from .models import Users, Profile, Products, Cart
from .serializers import UserSerializer, ProfileSerializer, ProductsSerializer, CartSerializer


# Create your views here.


class ShowAllProducts(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
