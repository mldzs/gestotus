# Generated by Django 3.0.8 on 2020-10-09 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='categoria',
            old_name='name',
            new_name='nome',
        ),
        migrations.RenameField(
            model_name='servico',
            old_name='name',
            new_name='nome',
        ),
    ]