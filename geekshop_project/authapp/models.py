from django.db import models

class Account(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='account', blank=True, null=True)
