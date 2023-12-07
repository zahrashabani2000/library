from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings


class Membership(models.Model):
    """Type of membership"""

    TYPE = (
        ('N','NORMAL'),
        ('G', 'GOLDEN')
        )


class BorrowerManager(BaseUserManager):
    """Manager for Cusomer class """

    def create_user(self, email, password, **extra_fields):
        """Creates a new user"""
        if not email:
            raise ValueError('User must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and save new superuser"""
        user = self.create_user(email, password, **extra_fields)

        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class Borrower(AbstractBaseUser, PermissionsMixin):
    """Difines a Borrower record in database"""

    email = models.EmailField(max_length=244, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField(
        default=False,
        help_text=("Designates whether the user can log into this admin site."),
    )
    
    objects = BorrowerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        """Return string representation of user"""
        return f"{self.first_name}, {self.last_name}"


class BorrowerFeedItem(models.Model):
    """Borrower info"""
    
    borrower_info = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    membership_type = models.CharField(choices=Membership.TYPE, max_length=50)
    registery_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.membership_type