# Generated by Django 2.0.6 on 2018-06-24 07:24

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SsrAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=30, verbose_name='SSR账户名')),
                ('ip', models.GenericIPAddressField(verbose_name='服务器IP')),
                ('port', models.CharField(max_length=10, verbose_name='账户端口')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'SSR账户信息',
                'verbose_name_plural': 'SSR账户信息',
            },
        ),
        migrations.CreateModel(
            name='SsrServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='服务器名称')),
                ('address', models.CharField(max_length=30, verbose_name='服务器归属地')),
                ('ip', models.GenericIPAddressField(verbose_name='服务器IP')),
                ('Weights', models.IntegerField(default=100, verbose_name='服务权重')),
                ('is_enable', models.BooleanField(default=False, verbose_name='服务器是否启用')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': 'SSR服务器',
                'verbose_name_plural': 'SSR服务器',
            },
        ),
    ]
