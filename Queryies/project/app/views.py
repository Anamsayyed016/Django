from django.shortcuts import render
from .models import Student
# Create your views here.

def student(request):
    # all_data = Student.objects.order_by('stu_name')  #accending  #id
    # all_data=Student.objects.order_by('-stu_name')   #decending   #-id
    # all_data=Student.objects.filter(stu_name='  max ')   #empty data return 
    # all_data=Student.objects.filter(stu_name='max',stu_email='anamsayyed58@gmail.com')    #empty data return 
    # all_data=Student.objects.filter(stu_name='anam',stu_email='anamsayyed58@gmail.com')    #single data return
    # all_data=Student.objects.exclude(stu_name='anam',stu_email='anamsayyed58@gmail.com')   #return not a given name values
    # all_data=Student.objects.get(stu_name = '')   #throwing error not giving empty set
    # all_data=Student.objects.first(stu_name = '')   #
    # all_data=Student.objects.last(stu_name = '')   #
    # all_data=Student.objects.create(stu_name = 'anam sayyed',stu_email="anamsayyed16@gmail.com",stu_contact=1254612,stu_city="bhopal")   # insert data in database

    data = Student.objects.first()
    # data.delete()

    # data.update(tu_name='anam',stu_email='anamsayyed58@gmail.com')
    data.stu_name="ali"
    data.stu_city="mumbai"
    data.save()


    # print(all_data)
    # print(all_data.values())
    # print(all_data.values_list())