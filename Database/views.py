from django.shortcuts import render,redirect
from .models import Students,Sliders

from django.contrib import messages

from django.core.paginator import Paginator 

#Authentication imports
from django.views.generic import CreateView
from .models import CustomUser
from .form import CustomUserChangeForm,CustomUserCreationForm 
from django.contrib.auth.views import LoginView 
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'Home.html')

def form(request):

    return render(request,'Form.html',{'navbar':'F orm'})

# def data(request):

#     #retrive data from the database and storing it in a variable called data
#     data = Students.objects.all()
#     return render(request,'viewdata.html',{'navbar':'data','data':data}) 

def data(request):

    paginate = Paginator(Students.objects.all(),1 )  
    page = request.GET.get('page')
    data = paginate.get_page(page)  
    return render(request,'viewdata.html',{'navbar':'data','data':data}) 

def delete(request,id):
    student=Students.objects.get(id=id)
    student.delete()
    messages.warning(request,"Data deleted")
    return redirect("/data")
    
def insertdata(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        if len(request.FILES) !=0:
            image=request.FILES['image']

            query= Students(name=name,email=email,phone=phone,image=image)
            query.save()

            messages.success(request,"data saved succesfully")

            return redirect("/data")
        
    return redirect("/data")

def edit(request,id):

    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        image=request.POST.get('image')
        
        student=Students.objects.get(id=id)

        student.name = name 
        student.email =email
        student.phone=phone
        student.image=image

        student.save()

        messages.success(request,"data updated succesfully")
        return redirect("/data")
      
    student=Students.objects.get(id=id)
    return render(request,'edit.html',{'student':student})
  
def sliders(request):
    slides= Sliders.objects.all()
    return render(request,"sliders.html",{"navbar":"sliders",'slides': slides})

def search(request):
     if request.method =='GET':
         query = request.GET.get('query')
         if query:
             student = Students.objects.filter(name__contains=query)
             return render(request,'search.html',{'data':student})
     return render(request, 'search.html') 

class SignUpview(CreateView):
    model = CustomUser
    form_class=CustomUserCreationForm
    success_url='/login/'
    template_name='register.html'

class UserLogin(LoginView):
    template_name='login.html'
