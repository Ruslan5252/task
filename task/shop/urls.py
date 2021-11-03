from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from shop.views import CategoryViewSet
from shop.views import ProductViewSet
from shop.views import ShopViewSet

router = DefaultRouter()
router.register('shops',ShopViewSet)
router.register('products',ProductViewSet)
router.register('categories',CategoryViewSet)

urlpatterns = [] + router.urls