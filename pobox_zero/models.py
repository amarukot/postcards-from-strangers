from django.db import models
from django.conf import settings


class Sender(models.Model):
    name = models.CharField(default='', max_length=100)

    def __str__(self):
        return self.name

class Postcard(models.Model):
    image_url = models.TextField(null=True, max_length=300)
    image = models.ImageField(default='', upload_to='images', blank=True)
    heading = models.CharField(default='', max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    favorited_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='favorited_by', blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


    # sender = models.ForeignKey(Sender, on_delete=models.CASCADE, related_name='postcards')
    # removed this relationship, believe it should be anonymous as per User Stories

    def __str__(self):
        return self.heading

