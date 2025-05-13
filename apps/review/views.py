from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Review
from .serializer import ReviewSerializer

