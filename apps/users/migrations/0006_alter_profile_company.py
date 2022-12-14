# Generated by Django 4.0.6 on 2022-07-25 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_company_cnpj'),
        ('users', '0005_alter_profile_is_active_alter_profile_photo_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_profiles', to='core.company', verbose_name='Companhia'),
        ),
    ]
