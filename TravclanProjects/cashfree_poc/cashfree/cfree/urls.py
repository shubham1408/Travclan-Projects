from cfree.views import *
from rest_framework import routers
from django.urls import path, include
router = routers.DefaultRouter()

# router.register(r'order', PaymentOrderViewset, basename='booking-payment')

urlpatterns = [
    path('', include(router.urls)),
    path('order', PaymentOrderAPI.as_view(), name="trjs"),

]