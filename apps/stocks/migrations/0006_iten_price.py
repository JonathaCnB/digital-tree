# Generated by Django 4.0.6 on 2022-07-29 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0005_alter_iten_options_alter_moviment_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='iten',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default='0.00', max_digits=7, null=True, verbose_name='Preço'),
        ),
    ]
