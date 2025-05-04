from django.db import models

# Create your models here.
class Department(models.Model):
    dep_name=models.CharField(max_length=20,unique=True)
    dep_desc=models.CharField(max_length=50)
    dep_hod=models.CharField(max_length=20)

    def __str__(self):
        return str(self.dep_name)
    

class Student(models.Model):
    stu_name=models.CharField(max_length=20)
    stu_email=models.EmailField()
    stu_contact=models.IntegerField()
    stu_dep=models.ForeignKey(Department,on_delete=models.PROTECT,to_field="dep_name",related_name="xyz")

    def __str__(self):
        return str(self.stu_name+" "+self.stu_email+" "+str)