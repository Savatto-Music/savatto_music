"""Users models"""

# Django
from django.contrib.auth.models import User
from django.db import models

GENRE_CHOICES = (
    ('pop','POP'),
    ('rock', 'ROCK'),
    ('salsa','SALSA'),
    ('urbano','URBANO'),
    ('popular','POPULAR'),
    ('son cubano','SON CUBANO'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=200, blank=True)
    genre = models.CharField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=200, blank=True)
    price = models.IntegerField(blank=True)
    genre = models.CharField(max_length=15, choices=GENRE_CHOICES, default='pop')

    picture = models.ImageField(
        upload_to='users/pictures', blank=True, null=True)

    def upload_to(instance, filename):
        return 'users/songs/{username}/{filename}'.format(
        username=instance.user.username, filename=filename)

    namesong1 = models.CharField(max_length=20, blank=True)
    urlsong1 = models.CharField(max_length=200, blank=True)

    namesong2 = models.CharField(max_length=20, blank=True)
    urlsong2 = models.CharField(max_length=200, blank=True)

    namesong3 = models.CharField(max_length=20, blank=True)
    urlsong3 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        """Return username"""
        return self.user.username
