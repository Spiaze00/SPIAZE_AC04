# Generated by Django 2.2.4 on 2019-09-18 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0008_orcamento_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orcamento',
            name='nome',
        ),
    ]