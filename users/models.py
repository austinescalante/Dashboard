from django.db import models
from django.contrib.auth.models import User

# Add profile picture


class Profile(models.Model):
    # One to one relationship with User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
