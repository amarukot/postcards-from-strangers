from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


# class Sender(models.Model):
#     name = models.CharField(default='', max_length=100)

#     def __str__(self):
#         return self.name


class Postcard(models.Model):
    image_url = models.TextField(null=True, max_length=300)
    image = models.ImageField(
        default='carousel-default.png', upload_to='images')
    heading = models.CharField(default='', max_length=255)
    message = models.TextField()
    created = models.DateTimeField(auto_now=True)
    favorited_by = models.ManyToManyField(
        User, related_name='favorited_by', blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='postcards')

    def __str__(self):
        return self.heading
