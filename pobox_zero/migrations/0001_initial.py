# Generated by Django 3.0.3 on 2020-02-18 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Postcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=300, null=True)),
                ('image', models.ImageField(blank=True, default='', upload_to='images')),
                ('heading', models.CharField(default='', max_length=255)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postcards', to='pobox_zero.Sender')),
            ],
        ),
    ]
