import datetime

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    USER_CHOICES = (
        ('1', 'Owner'),
        ('2', 'Tenant')
    )
    user_type = models.CharField(choices=USER_CHOICES, max_length=50,null=True)
    email = models.EmailField(verbose_name='email address', max_length=60, unique=True)
    username = models.CharField(max_length=40, unique=False)
    address = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=10, unique=False)
    city = models.CharField(max_length=60, null=True)
    aadhar = models.CharField(max_length=12, unique=True,null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_landowner= models.BooleanField(default=False)
    is_Tenant= models.BooleanField(default=False)



    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_landowner

    def has_module_perms(self, app_label):
        return True


class Watersources(models.Model):
    watersource_name=models.CharField(max_length=50)


class property(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    area=models.CharField(max_length=40, unique=False)
    city = models.CharField(max_length=255)
    images=models.FileField(upload_to=None)
    price=models.IntegerField(unique=True)
    description=models.CharField(max_length=255)
    TYPESOFSOIL_CHOICES = (
        ('c', 'Clay'),
        ('s', 'silt'),
        ('ch', 'chalk'),
        ('p', 'peat'),
        ('l', 'loam'),
    )
    type_of_soil=models.CharField(max_length=2, choices=TYPESOFSOIL_CHOICES)
    water=models.ForeignKey(Watersources,on_delete=models.CASCADE,null=True)


class Reviews(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    review=models.CharField(max_length=255)