from django.shortcuts import render, redirect, get_object_or_404

from .models import Employee, Position
from .forms import PositionForm, EmployeeForm


def index(request):
    employee_list = Employee.objects.raw('SELECT "jobs_employee"."id", "jobs_employee"."first_name", "jobs_employee"."last_name", "jobs_employee"."patronymic", "jobs_employee"."sex", "jobs_employee"."dob", "jobs_employee"."position_id", "jobs_position"."id", "jobs_position"."name", "jobs_position"."category" FROM "jobs_employee" LEFT OUTER JOIN "jobs_position" ON ("jobs_employee"."position_id" = "jobs_position"."id") ORDER BY "jobs_employee"."last_name" ASC, "jobs_employee"."first_name" ASC, "jobs_employee"."patronymic" ASC')
    # employee_list = Employee.objects.select_related('position')
    form = EmployeeForm()
    # positions_list = Position.objects.all()
    context = {'employee_list': employee_list, 'form': form}
    return render(request, 'jobs/index.html', context)


def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:index')
        return render(request, 'jobs/emp_create_update.html', {'form': form})
    return render(request, 'jobs/emp_create_update.html', {'form': form})


def employee_edit(request, employee_id):
    is_edit = True
    employee = get_object_or_404(Employee, id=employee_id)
    form = EmployeeForm(
        request.POST or None,
        instance=employee
    )
    if form.is_valid():
        form.save()
        return redirect('jobs:index')
    context = {'form': form, 'is_edit': is_edit}
    return render(request, 'jobs/emp_create_update.html', context)
