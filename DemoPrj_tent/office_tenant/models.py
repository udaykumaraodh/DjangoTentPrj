from django.db import models
from employee_shared.models import EmpDetails
# Create your models here.

class officeDetails(models.Model):
    empdet=models.ForeignKey(EmpDetails,on_delete=models.CASCADE)
    work=models.CharField(max_length=150)
