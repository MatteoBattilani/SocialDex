
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from .utils import sendTransaction
import hashlib

# Create your models here.
class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    datetime= models.DateTimeField(auto_now_add=True) # sets the time of the post to the time at which it was written
    content= models.TextField()
    hash = models.CharField(max_length=32, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def writeOnChain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
