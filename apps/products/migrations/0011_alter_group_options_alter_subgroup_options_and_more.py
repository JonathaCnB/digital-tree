# Generated by Django 4.0.6 on 2022-07-22 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_product_barcode_alter_group_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('name',), 'verbose_name': 'Grupo', 'verbose_name_plural': 'Grupos'},
        ),
        migrations.AlterModelOptions(
            name='subgroup',
            options={'ordering': ('name',), 'verbose_name': 'Sub Grupo', 'verbose_name_plural': 'Sub Grupos'},
        ),
        migrations.RenameField(
            model_name='group',
            old_name='group',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subgroup',
            old_name='sub_group',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='product',
            name='barcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Código de Barras'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_groups', to='products.subgroup', verbose_name='Sub Grupo'),
        ),
    ]
