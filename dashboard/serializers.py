from rest_framework import serializers
from .models import *
from rest_framework.fields import SerializerMethodField


class DeviceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ('id', 'device_type', 'created_at')


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ('id', 'action', 'code', 'created_at')


class DevicesSerializer(serializers.ModelSerializer):
    device_type = SerializerMethodField()

    class Meta:
        model = Device
        fields = ('id', 'device_name', 'device_type', 'phone', 'created_at')

    def get_device_type(mySerializer, myModel):
        return myModel.device_type.id
