from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderItemViewSet

router = DefaultRouter()
router.register(r'order-items', OrderItemViewSet, basename='orderitem')

app_name = 'orderitem'

urlpatterns = [
    path('', include(router.urls)),
]
