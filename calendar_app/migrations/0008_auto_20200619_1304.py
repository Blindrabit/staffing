# Generated by Django 3.0.3 on 2020-06-19 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendar_app', '0007_auto_20200619_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='manage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
