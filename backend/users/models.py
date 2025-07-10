import random
import re
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import ValidationError

# Custom manager to handle user creation
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and return a superuser with email, password, and other superuser privileges.
        """
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


# Custom User model using AbstractBaseUser
class User(AbstractBaseUser):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, null=False)
    email = models.EmailField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=False)  # Full admin privileges
    refreshtoken = models.CharField(max_length=2000,null=True)

    # Add the custom manager
    objects = UserManager()

    USERNAME_FIELD = 'email'  # Use email for authentication
    REQUIRED_FIELDS = []  # Only email is required for superuser creation

    def save(self, *args, **kwargs):
        """
        Save method for custom validations.
        """
        if not self.email:
            raise ValidationError('Email cannot be empty')
        super().save(*args, **kwargs)  # Call the parent save method

    def has_perm(self, perm, obj=None):
        """
        Custom permissions method.
        Superusers have all permissions.
        """
        return self.is_superuser

    def has_module_perms(self, app_label):
        """
        Custom module permissions method.
        Superusers have access to all modules.
        """
        return self.is_superuser
    
    @property
    def id(self):
        return self.userid
    
    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.email
    
class ForgotPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    token = models.CharField(max_length=6, unique=True)  # changed from UUIDField
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ForgotPassword for {self.user.email} - Token: {self.token}"

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = self.generate_token()
        super().save(*args, **kwargs)

    def generate_token(self):
        while True:
            token = f"{random.randint(100000, 999999)}"
            if not ForgotPassword.objects.filter(token=token).exists():
                return token

class Conversation(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1)
    conversationid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filePath = models.CharField(max_length=255)
    conversationName = models.CharField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        # Handle the filePath passed via kwargs, if provided
        filepath = kwargs.pop('filepath', None)
        if filepath:
            self.filePath = filepath
        
        # Set a default conversation name if it's blank
        if not self.conversationName:
            user_conversations = Conversation.objects.filter(userid=self.userid)
            next_number = user_conversations.count() + 1
            self.conversationName = f"New Conversation {next_number}"
        
        super().save(*args, **kwargs)  # Call the parent save method
