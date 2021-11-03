from rest_framework import serializers

from shop.models import Shop


class ShopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id',
                  'name',
                  )
class ShopCreateSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id',
                  'name')