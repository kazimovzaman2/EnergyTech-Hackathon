from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, abonet_code, password=None, **extra_fields):
        """
        Creates and saves a User with the given abonet_code and password.
        """
        if not abonet_code:
            raise ValueError('The Abonet Code field must be set')
        user = self.model(abonet_code=abonet_code, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, abonet_code, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given abonet_code and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(abonet_code, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    abonet_code = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'abonet_code'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.abonet_code

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        return self.abonet_code

    def get_short_name(self):
        return self.abonet_code


class Data(models.Model):
    used_date = models.JSONField()
    used_data = models.JSONField()
    predicted_date = models.JSONField()
    predicted_data = models.JSONField()

    def __str__(self):
        return self.used_data


class DataDate(models.Model):
    used_date = models.JSONField()
    used_data = models.JSONField()
    predicted_date = models.JSONField()
    predicted_data = models.JSONField()

    def __str__(self):
        return self.used_data
