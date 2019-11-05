# Generated by Django 2.2.6 on 2019-11-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=50)),
                ('nick_name', models.CharField(max_length=50)),
                ('pwd', models.CharField(max_length=50)),
                ('sex', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
            options={
                'db_table': 't_user',
            },
        ),
    ]