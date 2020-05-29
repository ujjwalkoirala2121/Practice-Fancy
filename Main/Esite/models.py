from django.db import models

# Create your models here.
class Shoes(models.Model):
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=100)

class Accessories(models.Model):
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=100)