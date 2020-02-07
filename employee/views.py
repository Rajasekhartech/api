from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def home(request):
    employee_list = Employee.objects.all()
    return render(request, 'emplist.html', {'elist' : employee_list })