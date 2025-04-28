from django.shortcuts import render
from rest_framework import viewsets
from .models import ClientSocialnetwork
from .serializer import ClientSocialnetworkSerializer
# Create your views here.
class ClientSocialnetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialnetwork.objects.all()
    serializer_class = ClientSocialnetworkSerializer