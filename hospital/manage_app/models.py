from django.db import models

# Create your models here.
class pationt_list(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    desease=models.CharField(max_length=20)
    pationt_type=models.CharField(max_length=20)


    