from django.db import models
from django.contrib.auth.models import User , auth
# Create your models here.
class Patients_appointment_Details(models.Model):
    Patient_id = models.IntegerField()
    Patient_name = models.CharField(max_length=255)
    Serious_illness = models.TextField()
    Allergies = models.TextField()
    Medical_history = models.TextField()
    Appointment_start = models.TimeField()
    Appointment_End = models.TextField()
    Priority = models.IntegerField()
    class Meta:
        db_table="Patient_Appointment_details"
    def str(self):
        return self.Patient_name


class Doctor_Details(models.Model):
    Patient_id = models.IntegerField()
    Appointment_id = models.IntegerField()
    patient_name = models.CharField(max_length=255)
    Appointment_start = models.TimeField()
    Appointment_End = models.TextField()
    Priority = models.IntegerField()
    class Meta:
        db_table = "Doctor_details"