# Generated by Django 2.2.2 on 2019-06-21 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0008_auto_20190621_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='part',
        ),
        migrations.AddField(
            model_name='usuario',
            name='participaciones',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='evento.Tipo_participacion'),
            preserve_default=False,
        ),
    ]