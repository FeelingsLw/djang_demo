from django.db import models

# Create your models here.
class Clazz(models.Model):
    name = models.CharField(max_length=50)
    count = models.IntegerField()

    class Meta:
        db_table = "t_clazz"