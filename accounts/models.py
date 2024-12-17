from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    vehicle = models.CharField(max_length=50)
    caption = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.vehicle
    

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    agreed_to_terms = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

