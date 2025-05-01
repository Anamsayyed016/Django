from django.db import models

# Create your models here.
class Aadhar(models.Model):
    aadhar=models.IntegerField(unique=True)
    create_date=models.DateField()
    created_by=models.CharField(max_length=20)

    def __str__(self):
        return str(self.aadhar)
    
    


class Student(models.Model):
    stu_name=models.CharField(max_length=20)
    stu_email=models.EmailField()
    stu_contant=models.IntegerField()
    aadhar_no=models.OneToOneField(Aadhar,on_delete=models.PROTECT,to_field='aadhar',related_name="xyz") #cascade

    def __str__(self):
        return self.stu_name + '' + str(self.aadhar_no)