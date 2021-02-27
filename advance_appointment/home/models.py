from django.db import models
from django.contrib.auth.models import User , auth
# Create your models here.

class Patients_login(models.Model):
    Email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    class Meta:
        db_table="Patient_details"