
# # def Register(request):
#     if request.method=="GET":
#         return render(request,"Registration.html")
# # def Home(request):
#     if request.method=="GET":
#         return render(request,"Home.html")
    
# # def Contactus(request):
#     if request.method=="GET":
#         return render(request,"Contactus.html")

# def Login(request):
#     if request.method=="GET":
#         return render(request,"Login.html")

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect,get_object_or_404
from django.contrib import messages
from User.models import Registration, UserQuery
# Create your views here.

def Home(request):
    return render(request,'Home.html')

def Register(request):
    if request.method == "POST":
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if firstname=="" and lastname=="" and email=="" and phone=="" and password=="":
            messages.error(request,'all field are required!')
            return redirect('signup')
        try:
            signup = get_object_or_404(Registration,Email=email)
            print(signup)
            print(email)
            print(signup.Email)
            if email == signup.Email:
                messages.error(request,'This email is already registered!')
                return redirect('signup')
        except Exception as e:
            print(e)
            Registration(First_name=firstname,Last_name=lastname,Email=email,Contact_no=phone,Password=password).save()
            messages.success(request,"Your account created successfully!")
            print('bye')
            return redirect('login')
    return render(request,"Registration.html")

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        password = request.POST.get('password')
        print(password)
        try:
            signup = Registration.objects.get(Email=email)
            if password == signup.Password:
                request.session['fullname'] = signup.First_name + ' ' + signup.Last_name
                request.session['email'] = signup.Email
                name = request.session.get('fullname')
                print(name)
                print(signup.Password)
                return redirect('profile')
            else:
                messages.error(request,'Wrong Password!')
                return redirect('login')
        except Exception as e:
            messages.error(request,'we are not able to find this email! please register first.')
            return redirect('login')
    return render(request,'login.html')

def profile(request):
    name = request.session.get('fullname')
    return render(request,'profile.html',{'name':name})

def logout(request):
    request.session.flush()
    messages.success(request,'You are logged out!')
    return redirect('login')

def Contactus(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        comment = request.POST.get('comment')
        UserQuery(name=name,email=email,query_desc=comment).save()
        return redirect('profile')
    return render(request,'contactus.html')

def Aboutus(request):
    if request.method== 'GET':
        return render(request,'About.html')