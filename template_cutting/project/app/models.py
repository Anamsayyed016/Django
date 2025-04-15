from django.db import models

# Create your models here.
class Student(models.Model):
    Stu_name = models.CharField(max_length=50)
    Stu_email = models.EmailField()
    Stu_contact = models.IntegerField(null=True)
    Stu_dis = models.CharField(max_length=201)
    Stu_dob = models.DateField()
    Stu_edu = models.CharField(max_length=50)
    Stu_gender = models.CharField(max_length=50)
    Stu_image = models.ImageField(upload_to='image/')
    Stu_document = models.FileField(upload_to='file/')
    Stu_pass = models.CharField(max_length=50)
    