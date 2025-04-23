from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Basefield)
class BaseInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','email','contact']

@admin.register(Student)
class BaseStudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','course','rollno','fees']

@admin.register(Employee)
class BaseEmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','contact','department','emp_id','salary']

@admin.register(Client)
class BaseClientAdmin(admin.ModelAdmin):
    project=models.CharField(max_length=50)
    list_display = ['id','name','email','contact','project','billing_status']