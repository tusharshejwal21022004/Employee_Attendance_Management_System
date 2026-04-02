from django.db import models

class Attendance(models.Model):
    employee_id = models.IntegerField()
    attendance_date = models.DateField()
    is_present = models.BooleanField(default=False)