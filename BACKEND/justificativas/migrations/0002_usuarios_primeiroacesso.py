# Generated by Django 4.0.6 on 2022-07-14 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justificativas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='primeiroAcesso',
            field=models.BooleanField(default=False),
        ),
    ]
