# Generated by Django 2.2.4 on 2019-09-18 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0005_orcamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamento',
            name='cod_orcamento',
            field=models.IntegerField(),
        ),
    ]
