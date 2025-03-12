# security_system/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('security', 'Security Personnel'),
        ('admin', 'Admin'),
        ('visitor', 'Visitor'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

# Visitor Model
class Visitor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    purpose = models.TextField()
    check_in_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Incident Model
class Incident(models.Model):
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Open')

    def __str__(self):
        return f'Incident {self.id} - {self.status}'

# Access Log Model
class AccessLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    area_accessed = models.CharField(max_length=200)
    access_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Access Log {self.id} - {self.area_accessed}'
