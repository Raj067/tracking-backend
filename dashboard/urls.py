from rest_framework.authtoken import views
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('get-device-types/', get_device_types, name="get_device_types"),

    path('token-auth/', TokenObtainPairView.as_view(), name='token_obtain_pair')
]
