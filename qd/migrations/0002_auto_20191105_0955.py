# Generated by Django 2.2.6 on 2019-11-05 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clazz', '0001_initial'),
        ('qd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qd',
            name='cid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='clazz.Clazz'),
        ),
        migrations.AlterField(
            model_name='qd',
            name='uid',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
        migrations.AlterModelTable(
            name='qd',
            table='t_qd',
        ),
    ]
