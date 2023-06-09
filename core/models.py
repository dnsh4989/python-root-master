from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
    

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_subscriber = False
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = True
        user.is_subscriber = False
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_subscriber = models.BooleanField(default=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    @property
    def name(self):
        return self.first_name + ' ' + self.last_name

    # @property
    # def revenue(self):
    #     orders = Order.objects.filter(user_id=self.pk, complete=True)
    #     return sum(o.ambassador_revenue for o in orders)


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500, null=True)
    image = models.FileField(upload_to='media/')
    thumbnail = models.FileField(upload_to='media/')
    content = models.TextField(max_length=20000, null=True)
    tags = models.TextField(max_length=200, null=True)