from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.


def get_device_types(request, *args, **kwargs):
    return JsonResponse(data={"name": "Rajabu"})
