from django.db import models

# Create your models here.
class Students(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField(max_length=50)
    stu_sno = models.IntegerField()
    stu_contact = models.IntegerField()
    stu_city = models.CharField(max_length=15)

    def __str__(self):
        return self.stu_name
    