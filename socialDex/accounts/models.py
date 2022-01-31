
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# class Profile will have one to one relationship with User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    last_login_IP = models.GenericIPAddressField(blank=True, null=True)
    alert = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk': self.pk})
