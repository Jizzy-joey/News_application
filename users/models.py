from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import Manger
# Create your models here.



class User(AbstractUser):
    USER_ROLES = (
        ('author', 'Author'),
        ('regular', 'Regular')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = None
    role = models.CharField(max_length=20, choices=USER_ROLES)

    USERNAME_FIELD = 'email' #which field is a unique identifier
    REQUIRED_FIELDS = []

    objects = Manger()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField()
    portfolio = models.TextField()
    reviews = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)