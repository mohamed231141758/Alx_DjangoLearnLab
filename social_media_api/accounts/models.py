from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom user model extending AbstractUser
class CustomUser(AbstractUser):
    # Bio field for user description
    bio = models.TextField(blank=True, null=True)
    # Profile picture field
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True
    )
    # Followers - self-referential ManyToMany relationship
    # symmetrical=False means following is one-directional
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following',
        blank=True
    )

    def __str__(self):
        return self.username
