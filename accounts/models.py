from django.db import models
from django.contrib.auth.models import User

class extendeduser(models.Model):
    fullname = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 54, default = 'abc@domain.com')
    role = models.CharField(max_length = 25)
    user = models.OneToOneField(User, on_delete=models.CASCADE)