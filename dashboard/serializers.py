from rest_framework import serializers
from .models import *


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ('id', 'device_type', 'created_at')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'action', 'code', 'created_at')
