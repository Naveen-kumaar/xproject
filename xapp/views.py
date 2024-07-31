from django.shortcuts import render,redirect
from xapp.models import register
from xapp.models import patientdetails

# Create your views here.
def home(request):
    return render(request,"home.html")
def create(request):
    
    if request.method == 'POST':
        date =request.POST.get('date')
        name =request.POST.get('name')
        age =request.POST.get('age')
        gender =request.POST.get('gender')
        address =request.POST.get('address')
        contactno =request.POST.get('contactno')
        history =request.POST.get('history')
        pain=request.POST.get('pain')
        duration=request.POST.get('duration')

        en =patientdetails(Date=date,Name=name,Age=age,Gender=gender,Address=address,Contactno=contactno,History=history,Pain=pain,Duration=duration)
        en.save()
        
        
    return render(request,"create.html")


def view(request):
    mydata=patientdetails.objects.all()

    return render(request,'view.html',{'data':mydata})



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