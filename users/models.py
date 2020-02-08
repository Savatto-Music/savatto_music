"""Users models"""

# Django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(blank=True)

    picture = models.ImageField(
        upload_to='users/pictures', blank=True, null=True)

    def upload_to(instance, filename):
        return 'users/songs/{username}/{filename}'.format(
        username=instance.user.username, filename=filename)

    namesong1 = models.CharField(max_length=20, blank=True)
    song1 = models.FileField(upload_to=upload_to, blank=True, null=True)

    namesong2 = models.CharField(max_length=20, blank=True)
    song2 = models.FileField(upload_to=upload_to, blank=True, null=True)

    namesong3 = models.CharField(max_length=20, blank=True)
    song3 = models.FileField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        """Return username"""
        return self.user.username
