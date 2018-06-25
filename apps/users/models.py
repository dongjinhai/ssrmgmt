from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女'),
    )
    nick_name = models.CharField(max_length=20, default="", verbose_name="昵称")
    birthday = models.DateField(blank=True, null=True, verbose_name="生日")
    gender = models.CharField(max_length=6, choices=gender_choices, default='male', verbose_name="性别")
    address = models.CharField(max_length=100, default="", verbose_name="地址")
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', default='image/default.png',
                              verbose_name="用户头像")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=10, verbose_name="验证码")
    email = models.EmailField(max_length=30, verbose_name="邮箱")
    type_choices = (
        ('register', '注册'),
        ('forget', '找回密码')
    )
    send_type = models.CharField(max_length=10, choices=type_choices, verbose_name="验证码类型")
    send_time = models.DateTimeField(default=datetime.now, verbose_name="发送时间")

    class Meta:
        verbose_name = "邮箱验证码"
        verbose_name_plural = verbose_name


