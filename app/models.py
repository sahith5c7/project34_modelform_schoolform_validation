from django.db import models

# Create your models here.
class School(models.Model):
    Sname=models.CharField(max_length=100,primary_key=True)
    Slocation=models.CharField(max_length=100)
    Sprincipal=models.CharField(max_length=100)
    email=models.EmailField()
    Reentermail=models.EmailField()

    def __str__(self):
        return self.Sname
        