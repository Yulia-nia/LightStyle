from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telephone = models.CharField(
        max_length=10,
        null=True,
    )
    # is_email_verified = models.BooleanField(default=False)


    class Meta:
        ordering = ['username', 'email']


class Avatar(models.Model):
    user = models.ForeignKey(User, related_name='avatars', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='img')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        get_latest_by = 'created_at'
        ordering = ['created_at']

    def __str__(self):
        return f'{self.user.username} avatar'

