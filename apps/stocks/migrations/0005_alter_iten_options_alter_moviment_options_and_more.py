# Generated by Django 4.0.6 on 2022-07-27 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_alter_iten_is_active_alter_moviment_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iten',
            options={'ordering': ('product', '-pk'), 'verbose_name': 'Iten', 'verbose_name_plural': 'Itens'},
        ),
        migrations.AlterModelOptions(
            name='moviment',
            options={'ordering': ('-pk',), 'verbose_name': 'Movimentação', 'verbose_name_plural': 'Movimentações'},
        ),
        migrations.AddField(
            model_name='iten',
            name='detail',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Detalhe'),
        ),
        migrations.AlterField(
            model_name='moviment',
            name='moviment',
            field=models.CharField(choices=[('e', 'Entrada'), ('s', 'Saida')], default='e', max_length=1, verbose_name='Movimento'),
        ),
    ]
