# Generated by Django 4.1.2 on 2022-12-20 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_devicetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='device_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.devicetype'),
        ),
    ]
