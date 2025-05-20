from django.db import models
from mentors_and_students.models import Mentor, Student
from django.contrib.auth.models import User

# Create your models here.
class Meet(models.Model):
    title = models.CharField(max_length=50)
    id_mentor = models.ForeignKey('mentors_and_students.Mentor', on_delete=models.PROTECT, null=False)
    id_student = models.ForeignKey('mentors_and_students.Student', on_delete=models.PROTECT, null=False)
    date_create = models.DateField(auto_now_add=True)
    date_meet = models.DateField()
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

