from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "t_user"
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)
    sex = models.IntegerField()
    phone = models.IntegerField()