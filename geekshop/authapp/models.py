from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    # SEX_MALE = 'male'
    # SEX_FEMALE = 'female'
    # SEX_OTHER = 'other'
    # SEX_CHOICE = (
    #     (SEX_MALE, 'Мужской'),
    #     (SEX_FEMALE, 'Женский'),
    #     (SEX_OTHER, 'другой')
    # )
    avatar = models.ImageField(upload_to='avatar', blank=True)
    age = models.PositiveSmallIntegerField(verbose_name='возвраст')
    # sex = models.CharField(max_length=6, choices=SEX_CHOICE, default=SEX_OTHER)
