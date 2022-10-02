from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from .models import ProductAndService, Reception, Cart, CartItem, Customer
from .serializers import ProductSerializer, \
    ReceptionSerializer,\
    CartSerializer,\
    CartItemSerializer,\
    AddCartItemSerializer,\
    UpdateCartItemSerializer,\
    CustomerSerializer


class ProductViewSet(ModelViewSet):
    queryset = ProductAndService.objects.all()
    serializer_class = ProductSerializer


class ReceptionViewSet(ModelViewSet):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer
    permission_classes = [IsAdminUser]


class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'patch', 'post', 'delete']
    queryset = CartItem.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}


class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'])
    def me(self, request):
        (customer, created) = Customer.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

