from django.shortcuts import render
from .models import ShopItem
from .serializers import ShopItemSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getAllItems(request):
    items = ShopItem.objects.all()
    serialized_items = ShopItemSerializer(items, many = True)
    return Response(serialized_items.data)