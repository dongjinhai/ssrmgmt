# Generated by Django 2.0.6 on 2018-07-14 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20180713_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodifyrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='账号'),
        ),
    ]