from django.db import models
from datetime import datetime

# Create your models here.
class datatables(models.Model):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    address=models.CharField(max_length=255 ,blank=True, null=True )
    phone=models.IntegerField(blank=True, null=True)
    noemp=models.IntegerField()
    date=models.DateField(blank=True, null=True)
    Price=models.IntegerField(blank=True,null=True)