# Generated by Django 2.2.2 on 2019-08-02 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0012_auto_20190802_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='dns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitio', models.CharField(max_length=1000)),
            ],
        ),
    ]
