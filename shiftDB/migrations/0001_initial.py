# Generated by Django 3.0.3 on 2020-06-19 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shifts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', multiselectfield.db.fields.MultiSelectField(choices=[('AE', 'A&E Nurse'), ('DR', 'Doctor')], default='Blank', max_length=5)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('manage', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]