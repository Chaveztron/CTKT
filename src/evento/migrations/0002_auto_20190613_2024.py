# Generated by Django 2.2.2 on 2019-06-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
