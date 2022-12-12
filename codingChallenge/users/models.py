from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class CustomBaseUserManager(BaseUserManager):
    def create_user(self, username, reference_id):
        if not username:
            raise ValueError('User must have a Username to login')
        if not reference_id:
            raise ValueError('User must have a Referende ID to login')

        user = self.model(
            username = username
        )

        user.set_password(raw_password=reference_id)
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, verbose_name='Username')
    reference_id = models.CharField(max_length=20, verbose_name='Password')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomBaseUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username