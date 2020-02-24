# Generated by Django 3.0.3 on 2020-02-24 16:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pobox_zero', '0004_remove_postcard_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcard',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]