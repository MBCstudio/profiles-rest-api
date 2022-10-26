from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

class UserProfileManager(AbstractBaseUser):
    """docstring fo UserProfileManager."""

    def create_user(self, name, email, password=None):
        """Funkcja tworzaca urzytkowanika"""
        if not email:
            raise ValueError("Użytkownik musi posiadać email")

        email = self.nozmalize_email(email)
        user = self.model(email=emali, name=name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, emali, password=None):
        """Funkcja tworzaca superurzytkowanika"""
        user = create_user(name,emali,password)

        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """docstring for UserProfile."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

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
