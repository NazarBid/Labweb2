from django.contrib.auth.models import AbstractUser
from django.db import models


class Agent(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    specialty = models.CharField(max_length=45)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Property(models.Model):
    type = models.CharField(max_length=45, null=True)
    address = models.CharField(max_length=45)
    price = models.IntegerField(null=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} {self.price}" if self.price is not None else self.type


class Client(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    contact_email = models.CharField(max_length=45)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Request(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self):
        return f"Request {self.id}"


class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('regular', 'Regular'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='regular')

    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    def __str__(self):
        return self.username