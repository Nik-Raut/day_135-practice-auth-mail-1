from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    student_name=models.CharField(max_length=30)
    student_marks=models.IntegerField()


