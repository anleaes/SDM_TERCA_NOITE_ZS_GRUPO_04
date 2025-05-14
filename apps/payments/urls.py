from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'payments'

router = routers.DefaultRouter()
router.register('', views.PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
   
]
