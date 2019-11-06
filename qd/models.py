from django.db import models
from user.models import User
from clazz.models import Clazz
# Create your models here


class Qd(models.Model):
    stage = models.CharField(max_length=100)
    progress = models.CharField(max_length=100)
    code_num = models.IntegerField()
    bug_num = models.IntegerField()
    remark = models.CharField(max_length=500)
    uid = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    create_time = models.CharField(max_length=100,default=None)
    class Meta:
        db_table = "t_qd"

