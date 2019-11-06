# Generated by Django 2.2.6 on 2019-11-05 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20191104_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(max_length=100)),
                ('progress', models.CharField(max_length=100)),
                ('code_num', models.IntegerField()),
                ('bug_num', models.IntegerField()),
                ('remark', models.CharField(max_length=500)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
