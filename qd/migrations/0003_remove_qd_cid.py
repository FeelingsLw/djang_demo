# Generated by Django 2.2.6 on 2019-11-06 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qd', '0002_auto_20191105_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qd',
            name='cid',
        ),
    ]
