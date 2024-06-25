from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class items(models.Model):
    productkey = models.CharField(max_length=20)
    name_of_the_product = models.CharField(max_length=100)
    description= models.TextField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name_of_the_product


    