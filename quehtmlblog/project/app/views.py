from django.shortcuts import render
from.models import Cooking

# Create your views here.
def index(request):
    return render(request,'index.html')

def home1(request,pk):
    userdata=Cooking.objects.get(id=pk)
    userdetails={
        "id":userdata.id,
        "name":userdata.cook_name,
        "email":userdata.cook_email,
        "foods":userdata.cook_foods,
        "cook_recipes":userdata.cook_recipes,
    }
    return render(request,'home.html',{"userdata":userdetails})

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def about1(request,pk):
    userdata=Cooking.objects.get(id=pk)
    userdetails={
        "id":userdata.id,
        "name":userdata.cook_name,
        "email":userdata.cook_email,
        "foods":userdata.cook_foods,
        "cook_recipes":userdata.cook_recipes,
    }
    return render(request,'about.html',{"userdata":userdetails})

def recipes(request):
    return render(request,'recipes.html')

def recipes1(request,pk):
    userdata=Cooking.objects.get(id=pk)
    userdetails={
        "id":userdata.id,
        "name":userdata.cook_name,
        "email":userdata.cook_email,
        "foods":userdata.cook_foods,
        "cook_recipes":userdata.cook_recipes,
    }
    return render(request,'recipes.html',{"userdata":userdetails})

def video(request):
    return render(request,'video.html')

def video1(request,pk):
    userdata=Cooking.objects.get(id=pk)
    userdetails={
        "id":userdata.id,
        "name":userdata.cook_name,
        "image":userdata.cook_image,
        "email":userdata.cook_email,
        "contact":userdata.cook_contact,
        "foods":userdata.cook_foods,
        "recipes":userdata.cook_recipes,
    }
    return render(request,'video.html',{"userdata":userdetails})


    

def register(request):
    return render(request,'register.html')

def registerdetail(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('cook_image')
        name = request.POST.get('cook_name')
        email = request.POST.get('cook_email')
        mobile = request.POST.get('cook_contact')
        food = request.POST.get('cook_foods')
        recipes = request.POST.get('cook_recipes')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        print(profile_pic, name, email, mobile, food, recipes, password, cpassword)

        user = Cooking.objects.filter(cook_email=email)
        if user:
            message = "Email is already exist"
            return render(request, "register.html", {'message': message})
        else:
            if password == cpassword:
                Cooking.objects.create(
                    cook_image=profile_pic,
                    cook_name=name,
                    cook_email=email,
                    cook_contact=mobile,
                    cook_foods=food,
                    cook_recipes=recipes,
                    cook_pass=password,
                )
                message = "Registration successful! Please login."
                return render(request, 'login.html', {'message': message})
            else:
                message = "your password did not match"
                return render(request, 'register.html', {'message': message})
    else:
        # Handle GET request
        return render(request, 'register.html')
    
def login(request):
    return render(request,'login.html')

def logiinfo(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Cooking.objects.get(cook_email=email)
        if user:
            userdata = Cooking.objects.get(cook_email=email)
            print(userdata.cook_email)
            print(userdata.cook_pass)
            passw = userdata.cook_pass

            if passw == password:
                message = "Welcome"
                userdetails = {
                    "id":userdata.id,
                    "name":userdata.cook_name,
                     "image":userdata.cook_image,
                     "email":userdata.cook_email,
                        "contact":userdata.cook_contact,
                         "foods":userdata.cook_foods,
                         "recipes":userdata.cook_recipes,
                }
                return render(request, 'dashboard.html', {'userdata': userdetails})
            else:
                message = "your email and password not exist"
                return render(request, 'login.html', {'message': message, 'email': email})
        else:
            message = "your email is not registered"
            return render(request, 'login.html', {'message': message, 'email': email})
    else:
        return render(request, 'login.html')
