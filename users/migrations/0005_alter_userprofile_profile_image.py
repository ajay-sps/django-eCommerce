# Generated by Django 4.2.2 on 2023-07-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_useraddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='/static/users/ritesh.jpg', upload_to='users/profile_images'),
        ),
    ]
