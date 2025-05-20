from django.db import models

# Create your models here.

class Bids(models.Model):
    title = models.CharField(max_length=50)
    id_mentor = models.ForeignKey('mentors_and_students.Mentor', on_delete=models.PROTECT, null=False)
    id_student = models.ForeignKey('mentors_and_students.Student', on_delete=models.PROTECT, null=False)
    date_create = models.DateField(auto_now_add=True)
    status_completed = models.BooleanField(default=False)