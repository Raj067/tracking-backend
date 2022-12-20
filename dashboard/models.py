from django.db import models
import uuid
# Create your models here.


class Device(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    device_name = models.CharField(max_length=100)
    device_type = models.ForeignKey(
        'DeviceType', on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=12)

    # Registration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_name}"

    class Meta:
        ordering = ("-id",)


class DeviceType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    device_type = models.CharField(max_length=100)
    # Registration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.device_type}"

    class Meta:
        ordering = ("-id",)


class Action(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    action = models.CharField(max_length=200)
    code = models.CharField(max_length=100)

    # Registration
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.action}"

    class Meta:
        ordering = ("-id",)
