from django.db import models
from django.conf import settings



class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name
# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(db_index=True)
    course=models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete = models.SET_NULL,
        related_name = 'students',
        null =True,
        blank = True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
        related_name = 'students',
        null =True,
        blank =True
    )

    def __str__(self):
        return self.name

