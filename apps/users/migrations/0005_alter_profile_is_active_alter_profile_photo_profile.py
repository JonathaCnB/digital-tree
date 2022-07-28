# Generated by Django 4.0.6 on 2022-07-21 13:09

import apps.users.models
from django.db import migrations, models
import utils.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(default='profile_default.png', null=True, upload_to=apps.users.models.upload_photo_company, validators=[utils.forms.photo_size], verbose_name='Foto'),
        ),
    ]
