from django.db import models
from accounts.managers import UserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    