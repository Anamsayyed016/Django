from django.shortcuts import render
from.models import Student

# Create your views here.
def home(request):
    return render(request,'base.html')

def index(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def registration(request):
    return render(request,'registration.html')

def login(request):
    return render(request,'login.html')

def register(request):
    print("register page")
    print(request.method)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    # print(request.META)
    username=request.POST.get('username')
    email=request.POST.get('email')
    detail=request.POST.get('detail')
    phone=request.POST.get('phone')
    dob=request.POST.get('dob')
    subscribe=request.POST.getlist('subscribe')
    gender=request.POST.get('gender')
    password=request.POST.get('password')
    cpassword=request.POST.get('cpassword')
    profile_pic=request.FILES.get('profile-pic')
    resume=request.FILES.get('resume')
    print(username,email,detail,phone,dob,subscribe,gender,password,cpassword,resume,profile_pic)

    Student.objects.create(Stu_name=username,
                          Stu_email=email,
                          Stu_contact=phone,
                          Stu_dis=subscribe,
                          Stu_dob=dob,
                          Stu_edu=detail,
                          Stu_image=profile_pic,
                        Stu_document=resume,
                        Stu_pass=password
                          )
