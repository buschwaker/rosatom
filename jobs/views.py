from django.shortcuts import render

from .models import Employee, Position
from .forms import PositionForm, EmployeeForm


def index(request):
    employee_list = Employee.objects.raw(
        'SELECT * FROM "jobs_employee" LEFT OUTER JOIN "jobs_position" ON'
        ' ("jobs_employee"."position_id" = "jobs_position"."id") ORDER BY '
        '"jobs_employee"."last_name" ASC, "jobs_employee"."first_name" ASC, '
        '"jobs_employee"."patronymic" ASC'
    )
    form = EmployeeForm()
    # positions_list = Position.objects.all()
    context = {'employee_list': employee_list, 'form': form}
    return render(request, 'jobs/index.html', context)
