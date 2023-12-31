# Generated by Django 4.2.3 on 2023-07-21 21:37

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_user_avatar_remove_user_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=users.models.get_file_path),
        ),
        migrations.AddField(
            model_name='user',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='website',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
