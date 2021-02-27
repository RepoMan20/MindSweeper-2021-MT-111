from django.contrib import admin

# Register your models here.
from home.models import *
admin.site.register(Patients_appointment_Details)
admin.site.register(Doctor_Details)