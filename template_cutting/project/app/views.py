from django.shortcuts import render
from .models import Student

# Home page
def home(request):
    return render(request, 'home.html')

# ===================== index ============================
def index(request, pk):
    user = Student.objects.get(id=pk)
    userdata = {
        "id": user.id,
        "name": user.Stu_name,
        "contact": user.Stu_contact,
        "dis": user.Stu_dis,
        "dob": user.Stu_dob,
        "email": user.Stu_email,
        "image": user.Stu_image,
        "file": user.Stu_document,
        "gender": user.Stu_gender,
        "password": user.Stu_pass,
        "education": user.Stu_edu,
    }
    return render(request, 'home.html', {'userdata': userdata})

# ===================== about ============================
def about(request):
    return render(request, 'about.html')

def about1(request, pk):
    user = Student.objects.get(id=pk)
    userdata = {
        "id": user.id,
        "name": user.Stu_name,
        "contact": user.Stu_contact,
        "dis": user.Stu_dis,
        "dob": user.Stu_dob,
        "email": user.Stu_email,
        "image": user.Stu_image,
        "file": user.Stu_document,
        "gender": user.Stu_gender,
        "password": user.Stu_pass,
        "education": user.Stu_edu,
    }
    return render(request, 'about.html', {'userdata': userdata})

# ===================== contact ============================
def contact(request):
    return render(request, 'contact.html')

def contact1(request, pk):
    user = Student.objects.get(id=pk)
    userdata = {
        "id": user.id,
        "name": user.Stu_name,
        "contact": user.Stu_contact,
        "dis": user.Stu_dis,
        "dob": user.Stu_dob,
        "email": user.Stu_email,
        "image": user.Stu_image,
        "file": user.Stu_document,
        "gender": user.Stu_gender,
        "password": user.Stu_pass,
        "education": user.Stu_edu,
    }
    return render(request, 'contact.html', {'userdata': userdata})

# ===================== services ============================
def services(request):
    return render(request, 'services.html')

def services1(request, pk):
    user = Student.objects.get(id=pk)
    userdata = {
        "id": user.id,
        "name": user.Stu_name,
        "contact": user.Stu_contact,
        "dis": user.Stu_dis,
        "dob": user.Stu_dob,
        "email": user.Stu_email,
        "image": user.Stu_image,
        "file": user.Stu_document,
        "gender": user.Stu_gender,
        "password": user.Stu_pass,
        "education": user.Stu_edu,
    }
    return render(request, 'services.html', {'userdata': userdata})

# ===================== registration ============================
def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

# ===================== register logic ============================
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        detail = request.POST.get('detail')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        subscribe = request.POST.getlist('subscribe')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        profile_pic = request.FILES.get('profile-pic')
        resume = request.FILES.get('resume')

        user = Student.objects.filter(Stu_email=email)
        if user.exists():
            msg = "Email already exists"
            return render(request, 'registration.html', {'key': msg})
        else:
            if password == cpassword:
                Student.objects.create(
                    Stu_name=username,
                    Stu_email=email,
                    Stu_contact=phone,
                    Stu_dis=subscribe,
                    Stu_dob=dob,
                    Stu_edu=detail,
                    Stu_image=profile_pic,
                    Stu_document=resume,
                    Stu_pass=password
                )
                msg = "Registration successful"
                return render(request, 'login.html', {'key': msg})
            else:
                msg = "Password and Confirm Password do not match"
                return render(request, 'registration.html', {'key': msg})
    else:
        return render(request, 'registration.html')

# ===================== login data logic ============================
def logindata(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        passw = request.POST.get('password')

        try:
            user = Student.objects.get(Stu_email=email)
            if passw == user.Stu_pass:
                userdata = {
                    "id": user.id,
                    "name": user.Stu_name,
                    "contact": user.Stu_contact,
                    "dis": user.Stu_dis,
                    "dob": user.Stu_dob,
                    "email": user.Stu_email,
                    "image": user.Stu_image,
                    "file": user.Stu_document,
                    "education": user.Stu_edu,
                    "password": user.Stu_pass,
                }
                msg = "Welcome to dashboard"
                return render(request, 'dashboard.html', {'userdata': userdata, 'msg': msg})
            else:
                msg = "Incorrect password"
                return render(request, 'login.html', {'msg': msg, 'email': email})
        except Student.DoesNotExist:
            msg = "Email not registered"
            return render(request, 'login.html', {'msg': msg, 'email': email})
    else:
        return render(request, 'login.html')
