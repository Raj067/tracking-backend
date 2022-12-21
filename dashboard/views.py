from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def get_device_types(request, *args, **kwargs):
    data = DeviceType.objects.all()
    serializer = DeviceTypeSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_possible_actions(request, *args, **kwargs):
    data = Action.objects.all()
    serializer = ActionSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_devices(request, id, *args, **kwargs):
    data = [i for i in Device.objects.all() if str(i.device_type.id) == id]
    serializer = DevicesSerializer(data, many=True)
    return Response(serializer.data)
