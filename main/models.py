from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobilenumber = models.CharField(max_length=15)
    qualification =models.IntegerField()
    jobrole =models.CharField(max_length=100)
    experience =models.IntegerField()
    resume =models.FileField(upload_to='resumes/')

    class Meta:
        db_table='student_details'
        
