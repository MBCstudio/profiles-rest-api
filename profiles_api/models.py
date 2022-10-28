from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserProfileManager(BaseUserManager):
    """docstring fo UserProfileManager."""

    def create_user(self, name, email, password=None):
        """Funkcja tworzaca urzytkowanika"""
        if not email:
            raise ValueError("Użytkownik musi posiadać email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None):
        """Funkcja tworzaca superużytkowanika"""
        user = self.create_user(name,email,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """docstring for UserProfile."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Podaje pełną nazwę użytkownika"""
        return self.name

    def get_short_name(self):
        """Podaje skrócone imie użytkownika"""
        return self.name

    def __str__(self):
        """Podaje str profilu uzytkownika np.mail"""
        return self.email
