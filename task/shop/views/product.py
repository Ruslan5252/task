from rest_framework.viewsets import mixins, GenericViewSet
from shop.serializers import ProductListSerializer,ProductCreateSerializer
from rest_framework.permissions import AllowAny
from shop.models.product import Product
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny, ]
    queryset = Product.objects.all()


    def get_serializer_class(self):
        serializer_class = ProductListSerializer
        if self.action == 'create':
            serializer_class = ProductCreateSerializer
        elif self.action == 'list':
            serializer_class = ProductListSerializer
        return serializer_class


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.all()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
