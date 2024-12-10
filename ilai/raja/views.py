from django.shortcuts import render,redirect
from .forms import MyForm
from django.contrib import messages
from .models import RegisterForm

# Create your views here.
def home(request):

    data=RegisterForm.objects.all()
    if(data!=''):
        return render(request,"home.html",{'data':data})
    else:
        return render(request,"home.html")

def insert(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Register successfully Completed")
                return redirect("home")
            except:
                pass
    else:
        form=MyForm()
        return render(request,"register.html",{'form':form})


def update(request,id):
    data=RegisterForm.objects.get(id=id)
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        contact=request.POST['contact']
        email=request.POST['email']

        data.name=name
        data.age=age
        data.address=address
        data.contact=contact
        data.email=email
        data.save()
        messages.success(request,"Update Successfully Completed")
        return  redirect("home")

    return render(request,"update.html",{'data':data})

def delete(request,id):
    data=RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request,"Delete Successfully Completed")
    return redirect("home")

