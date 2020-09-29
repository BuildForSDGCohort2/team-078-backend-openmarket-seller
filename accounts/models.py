from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password=None):
       # Creates and saves a User with the given email, phone number and password
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), first_name=first_name, last_name=last_name, phone_number=phone_number,)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password=None):
        # Creates and saves a superuser with the given email, phone number and password
        user = self.create_user(email, first_name=first_name, last_name=last_name, password=password, phone_number=phone_number,)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    # Create a user with email address and phone number
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True,)
    phone_number = models.CharField(max_length=225)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name','phone_number']

    def __str__(self):
        # String
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin