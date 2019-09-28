from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class UserProfileManager(BaseUserManager):
    """ helps django work with our Userprofile model"""

    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValueError("L'utilisateur doit avoir une addresse email valide")
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name)

        user.set_password(password)
        user.save(using=self._db) 
        return user
    
    def create_superuser(self, email, first_name, last_name, password):
        """used to create a staff user"""
        user = self.create_user(email, first_name, last_name, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db) 
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """this is our custum user profile inside our system"""
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def get_short_name(self):
        """used to get a users first name"""
        return self.first_name

    
    