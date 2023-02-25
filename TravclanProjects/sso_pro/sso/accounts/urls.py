from accounts.api.views import UserProfileAPIView
from rest_framework import routers
from django.urls import path, include
router = routers.DefaultRouter()

# router.register(r'api/v1/me', UserProfileAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('sso/sucess', UserProfileAPIView.as_view(), name='my_profile'),
]