from django.shortcuts import render, redirect
from Emp_management.forms import EmployeeForm
from Emp_management.models import Employee
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        print(form)
        form.save()
        if form.is_valid():
            try:
                form.save()
                return redirect('/admin/show')
            except:
                return HttpResponse('<h1>ERROR<h1>')
    else:
        form = EmployeeForm()
    return render(request, 'html/insert.html', {'form': form})


def show(request):
    employees = Employee.objects.all()
    count = Employee.objects.count()
    # print(employees)
    return render(request, "html/employee.html", {'employees': employees, 'count': count, })


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'html/edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    form.save()
    print(form)
    if form.is_valid():
        form.save()
        return redirect("/admin/show")
    return render(request, 'html/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/admin/show")


def signin(request):
    emp = Employee.objects.count()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        form = EmployeeForm()
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return render(request, 'html/adminpanel.html', {'form': form, 'count': emp})
        elif Employee.objects.filter(email=username, password=password).exists():
            return render(request, 'html/dashboard.html', {'name': username})
        else:

            return render(request, 'html/signin.html', {'message': 'Invalid Username/Password'})

    return render(request, 'html/adminpanel.html', {'count': emp})


def admin(request):
    return render(request, 'html/adminpanel.html')


def home(request):
    return render(request, 'html/index.html')


def insert(request):
    form = EmployeeForm()
    return render(request, 'html/insert.html', {'form': form})


# def empChecking(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         if Employee.objects.filter(email=email, password=password).exists():
#             return render(request, 'html/dashboard.html',{'name':email})
#
#         else:
#
#             return render(request, 'html/empsignin.html', {'message': 'Invalid Username/Password'})
#     return render(request, 'html/empsignin.html')

def signinPage(request):
    return render(request, 'html/signin.html')


def dashboard(request):
    emp = EmployeeForm.objects.count()
    return render(request, 'html/adminpanel.html', {'emp': emp})


def signout(request):
    auth.logout(request)
    return render(request, 'html/signin.html')
