from pickle import TRUE
from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from productApp.models import Card
from rest_framework.response import Response

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email = email ,username = email, **extra_fields)
        user.is_seller = False
        user.is_active = True
        user.set_password(password)
        user.save()
        return user
        

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if not (extra_fields.get('is_staff') or extra_fields.get('is_superuser')):
            raise ValueError('Superuser must have is_staff=True and is_superuser=True')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    first_name = models.CharField(verbose_name ='First name', max_length=150, blank=True)
    last_name = models.CharField(verbose_name = 'Last name', max_length=150, blank=True)
    email = models.EmailField(verbose_name="Email address" , blank=False, unique=True, null=False)
    is_active = models.BooleanField(default=False)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, blank=True, null=True ,verbose_name='Card')
    is_seller = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name' , 'last_name' , 'password']
    
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

# Create your models here.
