# Generated by Django 2.2.6 on 2019-11-06 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clazz', '0001_initial'),
        ('user', '0002_auto_20191104_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clazz.Clazz'),
        ),
    ]