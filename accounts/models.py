from pyexpat import model
from django.db import models 
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Clientt(AbstractUser):

    b_o_b = models.CharField(max_length=2) 

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]



