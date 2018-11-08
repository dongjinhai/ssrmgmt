# Generated by Django 2.0.6 on 2018-10-26 19:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataUsageRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bytes_recv', models.CharField(max_length=20, verbose_name='收到的数据')),
                ('bytes_sent', models.CharField(max_length=20, verbose_name='发送的数据')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='node.Node', verbose_name='节点')),
            ],
            options={
                'verbose_name': '用户流量使用情况',
                'verbose_name_plural': '用户流量使用情况',
            },
        ),
    ]