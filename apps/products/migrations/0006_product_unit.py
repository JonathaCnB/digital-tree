# Generated by Django 4.0.6 on 2022-07-19 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_group_table_alter_subgroup_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('b', 'Caixa'), ('kg', 'Quilograma'), ('g', 'Grama'), ('und', 'Unidade')], default='und', max_length=3),
        ),
    ]
