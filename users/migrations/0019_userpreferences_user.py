# Generated by Django 3.2.6 on 2021-08-22 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210822_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreferences',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
