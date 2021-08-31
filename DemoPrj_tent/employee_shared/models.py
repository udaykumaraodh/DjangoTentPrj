from django.db import models

# Create your models here.

class EmpDetails(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=150)
    salary=models.FloatField()


    def __str__(self) :
        return self.ename
