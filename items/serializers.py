from rest_framework.serializers import ModelSerializer
from .models import ShopItem

class ShopItemSerializer(ModelSerializer):
    class Meta:
        model = ShopItem
        fields = '__all__'
        depth = 1