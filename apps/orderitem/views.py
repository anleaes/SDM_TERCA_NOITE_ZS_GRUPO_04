from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import OrderItem
from .serializers import OrderItemSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer