from django.shortcuts import render
from.models import Student

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request,pk):
    userdata=Student.objects.get(id=pk)
    userdata={

                "id":userdata.id,
                "name":userdata.Stu_name,
                "contact":userdata.Stu_contact,
                "dis":userdata.Stu_dis,
                "dob":userdata.Stu_dob,
                "email":userdata.Stu_email,
                "image":userdata.Stu_image,
                "file":userdata.Stu_document,
                "gender":userdata.Stu_gender,
                "password":userdata.Stu_pass,
                "education":userdata.Stu_edu,
    }
    return render(request,'home.html',{'userdata':userdata})


def about(request):
    userdata=Student.objects.get(id=8)
    userdata={

                "id":userdata.id,
                "name":userdata.Stu_name,
                "contact":userdata.Stu_contact,
                "dis":userdata.Stu_dis,
                "dob":userdata.Stu_dob,
                "email":userdata.Stu_email,
                "image":userdata.Stu_image,
                "file":userdata.Stu_document,
                "gender":userdata.Stu_gender,
                "password":userdata.Stu_pass,
                "education":userdata.Stu_edu,
    }
    return render(request,'about.html',{'userdata':userdata})

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

    
    user=Student.objects.filter(Stu_email=email)
    if user:
        msg="Email exist"
        return render(request,'registration.html',{'key':msg})
    
    else:
        if password==cpassword:
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
            msg="regis done"
            return render(request,'login.html',{'key':msg})
        else:
            msg="pass and cpass not match"
            return render(request,'registration.html',{'key':msg})
        


            # {% comment %} login dataaaa {% endcomment %}

def logindata(request):
    if request.method=='POST':
        email=request.POST.get('email')
        passw=request.POST.get('password')

        user=Student.objects.filter(Stu_email=email)
        if user:
            userdata=Student.objects.get(Stu_email=email)
            print(userdata.Stu_name)
            print(userdata.Stu_email)
            pass1=userdata.Stu_pass

            if passw==pass1:
                msg="welcome to dashboard"
                userdata={
                    "id":userdata.id,
                    "name":userdata.Stu_name,
                    "contact":userdata.Stu_contact,
                    "dis":userdata.Stu_dis,
                    "dob":userdata.Stu_dob,
                    "email":userdata.Stu_email,
                    "image":userdata.Stu_image,
                    "file":userdata.Stu_document,
                    "education":userdata.Stu_edu,
                    "password":userdata.Stu_pass,   
                    
                }
                return render(request,'dashboard.html',{'userdata':userdata})

            else:
                msg="email & password not exist"
                return render(request,'login.html',{'msg':msg,'email':email})
            
        else:
            msg="email not registered"
            return render(request,'login.html',{'msg':msg,'email':email})
    
    else:
        return render(request,'login.html')
