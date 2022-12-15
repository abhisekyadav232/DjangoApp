# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect  
from employee.forms import EmployeeForm  
from employee.models import Employee  
# Create your views here. 
print("sunil testing")  
def emp(request):
    # print("request.method " + request.method)
    if request.method == "POST": 
        form = EmployeeForm(request.POST)
          
        

        try:  
            form.save()  
            return redirect('/show')  
        except: 
            pass
    else:  
        form = EmployeeForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")  
def ab(request):
    return render(request,"ab.html")
def index1(request):
    return render(request,"index.html")