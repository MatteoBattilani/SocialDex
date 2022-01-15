from django.contrib.auth import user_logged_in
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from ipware import get_client_ip

from redis import Redis
from datetime import date, timedelta

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(user_logged_in, sender=User)
def save_profile(sender, request, user, **kwargs):

    """
    redis_client = Redis('localhost', port=6379)

    yesterday = date.today() - timedelta(days=1)
    list_name = yesterday.strftime('%d/%m/%Y')
    redis_key = redis_client.lrange(list_name, 0, -1)
    """
    ip, is_routable = get_client_ip(request)
    profile = Profile.objects.get(user=user)

    if profile.last_login_IP == ip or profile.last_login_IP is None:
        profile.alert = False
    else:
        profile.alert = True
    profile.last_login_IP = ip
    profile.save()

