# Generated by Django 4.2.3 on 2023-07-21 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_avatar_user_description_user_webisite_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
