# Generated by Django 4.0 on 2022-06-12 18:32

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('reviewdeck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
                ('url', models.URLField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('technologies', models.CharField(blank=True, max_length=200)),
                ('photo', pyuploadcare.dj.models.ImageField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='auth.user')),
            ],
        ),
    ]
