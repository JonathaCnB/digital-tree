# Generated by Django 4.0.6 on 2022-07-20 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0002_alter_moviment_profile_iten'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviment',
            old_name='unit',
            new_name='moviment',
        ),
    ]
