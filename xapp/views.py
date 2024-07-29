from django.shortcuts import render
from xapp.models import register

# Create your views here.
def home(request):
    return render(request,"home.html")
def create(request):
    return render(request,"create.html")
def view(request):
    return render(request,"view.html")
def Register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        role = request.POST.get('role')
        Password = request.POST.get('Password')
        C_Password = request.POST.get('C_Password')
        en = register(name=name,email=email,mobile=mobile,role=role,Password=Password,C_Password=C_Password)
        en.save()

        # myuser= User.objects.create_user(name,email,mobile,role,Password,C_Password)
        # myuser.save()



        
    return render(request,"register.html")