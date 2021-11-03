from rest_framework.viewsets import mixins, GenericViewSet
from shop.serializers import CategoryListSerializer, CategoryCreateSerializer
from rest_framework.permissions import AllowAny
from shop.models.categories import Category
from rest_framework.response import Response
from rest_framework import status

class CategoryViewSet(mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      GenericViewSet):
    serializer_class = CategoryListSerializer
    permission_classes = [AllowAny, ]
    queryset = Category.objects.all()


    def get_serializer_class(self):
        serializer_class = CategoryListSerializer
        if self.action == 'create':
            serializer_class = CategoryCreateSerializer
        elif self.action == 'list':
            serializer_class = CategoryListSerializer
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
