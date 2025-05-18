from django.shortcuts import render,redirect,get_object_or_404
from employeapp.models import Employee,Company
from employeapp.forms import EmployeForm,CompanyForm,RegistrationForm,LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
def companyadd(request):
    if request.method=='POST':
        comp=CompanyForm(request.POST)
        if comp.is_valid():
            comp.save()
            return redirect('companylist')
    else:
        comp=CompanyForm()
    return render(request,'companyadd.html',{'comp':comp})
def companylist(request):
    comp=Company.objects.all()
    return render(request,'companylist.html',{'comp':comp})

def employeadd(request):
    if request.method=='POST':
        emp=EmployeForm(request.POST)
        if emp.is_valid():
            emp.save()
            return redirect('employeelist')
    else:
        emp=EmployeForm()
    return render(request,'employeadd.html',{'emp':emp})
def employeupdate(request,pk):
    emp=get_object_or_404(Employee,id=pk)
    if request.method=='POST':
        emp=EmployeForm(request.POST,instance=emp)
        if emp.is_valid():
            emp.save()
            return redirect('employeelist')
    else:
        emp=EmployeForm(instance=emp)
    return render (request,'employeupdate.html',{'emp':emp})
def companyupdate(request,pk):
    comp=get_object_or_404(Company,id=pk)
    if request.method=='POST':
        comp=CompanyForm(request.POST,instance=comp)
        if comp.is_valid():
            comp.save()
            return redirect('companylist')
    else:
        comp=CompanyForm(instance=comp)
    return render(request,'companyupdate.html',{'comp':comp})
def deletecomp(request,pk):
    comp=get_object_or_404(Company,id=pk)
    comp.delete()
    redirect('companylist')
    return render(request,'delete.html',)
def employelist(request):
    emp=Employee.objects.all()
    return render(request,'employelist.html',{'emp':emp})
def registrationview(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('employeelist')  # Replace 'home' with your homepage view name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logoutview(request):
    logout(request)
    return redirect('login')
