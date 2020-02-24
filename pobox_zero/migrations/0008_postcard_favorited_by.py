# Generated by Django 3.0.3 on 2020-02-24 19:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pobox_zero', '0007_remove_postcard_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
