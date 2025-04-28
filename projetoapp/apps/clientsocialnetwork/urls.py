from django.urls import path, include
from rest_framework import routers
from .views import ClientSocialnetworkViewSet

app_name = 'clientsocialnetwork'

router = routers.DefaultRouter()
router.register('', ClientSocialnetworkViewSet, basename='clientsocialnetwork')

urlpatterns = [
    path('', include(router.urls)),
    
]