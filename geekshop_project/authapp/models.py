from django.db import models

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account', blank=True, null=True)
