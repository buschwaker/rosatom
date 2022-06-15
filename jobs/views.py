from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Employee, Position
from .forms import PositionForm, EmployeeForm


@login_required
def index(request):
    """
    Обрабатывает запрос к главной странице сайта выводит список должностей
    и сотрудников, доступно аутентифицированному пользователю
    """
    search_position = request.GET.get('q_position')
    search_employee = request.GET.get('q_employee')
    print(search_employee)
    if not search_employee or search_employee == '':
        employee_list = Employee.objects.raw(
            'SELECT "jobs_employee"."id" as "employee_id", "jobs_employee".'
            '"first_name", "jobs_employee"."last_name", "jobs_employee".'
            '"patronymic", "jobs_employee"."sex", "jobs_employee"."dob", '
            '"jobs_employee"."position_id", "jobs_position"."id", '
            '"jobs_position"."name", "jobs_position"."category" FROM '
            '"jobs_employee" LEFT OUTER JOIN "jobs_position" ON '
            '("jobs_employee"."position_id" = "jobs_position"."id") ORDER BY'
            ' "jobs_employee"."last_name" ASC, '
            '"jobs_employee"."first_name" ASC,'
            ' "jobs_employee"."patronymic" ASC'
        )
    else:
        search_employee = "%s%%" % search_employee.capitalize()
        employee_list = Employee.objects.raw(
            'SELECT "jobs_employee"."id" as "employee_id", "jobs_employee"'
            '."first_name", "jobs_employee"."last_name", "jobs_employee".'
            '"patronymic", "jobs_employee"."sex", "jobs_employee"."dob", '
            '"jobs_employee"."position_id", "jobs_position"."id", '
            '"jobs_position"."name", "jobs_position"."category" FROM '
            '"jobs_employee" LEFT OUTER JOIN "jobs_position" ON '
            '("jobs_employee"."position_id" = "jobs_position"."id") '
            'WHERE "jobs_employee"."last_name" LIKE %s ORDER BY '
            '"jobs_employee"."last_name" ASC, "jobs_employee"."first_name"'
            ' ASC, "jobs_employee"."patronymic" ASC', [search_employee]
        )
    if not search_position or search_position == '':
        positions_list = Position.objects.raw(
            'SELECT * FROM "jobs_position" ORDER'
            ' BY "jobs_position"."name" ASC'
        )
    else:
        search_position = "%s%%" % search_position.capitalize()
        positions_list = Position.objects.raw(
            'SELECT * FROM "jobs_position" '
            'WHERE "jobs_position"."name" LIKE %s '
            'ORDER BY "jobs_position"."name" ASC', [search_position]
        )
    context = {
        'employee_list': employee_list,
        'positions_list': positions_list,
    }
    return render(request, 'jobs/index.html', context)


@user_passes_test(lambda u: u.is_staff)
def create_employee(request):
    """
    Функция создает пользователя,
    доступно пользователю с административными правами
    """
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jobs:index')
        return render(request, 'jobs/emp_create_update.html', {'form': form})
    return render(request, 'jobs/emp_create_update.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def employee_edit(request, employee_id):
    """
    Функция изменяет данные пользователя,
    доступно пользователю с административными правами
    """
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


@user_passes_test(lambda u: u.is_staff)
def employee_delete(request, employee_id):
    """
    Функция удаляет данные пользователя,
    доступно пользователю с административными правами
    """
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('jobs:index')


@user_passes_test(lambda u: u.is_staff)
def position_create(request):
    """
    Функция создает должность,
    доступно пользователю с административными правами
    """
    form = PositionForm()
    if request.method == 'POST':
        form = PositionForm(request.POST)
        if form.is_valid():
            Position.objects.create(
                name=form.cleaned_data['name'],
                category=form.cleaned_data['category'],
            )
            return redirect('jobs:index')
    return render(request, 'jobs/emp_create_update.html', {'form': form})


@user_passes_test(lambda u: u.is_staff)
def position_edit(request, position_id):
    """
    Функция изменяет данные о должности,
    доступно пользователю с административными правами
    """
    is_edit = True
    position = get_object_or_404(Position, id=position_id)
    form = PositionForm(
        request.POST or None,
        instance=position
    )
    if form.is_valid():
        form.save()
        return redirect('jobs:index')
    context = {'form': form, 'is_edit': is_edit}
    return render(request, 'jobs/emp_create_update.html', context)


@user_passes_test(lambda u: u.is_staff)
def position_delete(request, position_id):
    """
    Функция удаляет данные о должности,
    доступно пользователю с административными правами
    """
    position = get_object_or_404(Position, id=position_id)
    position.delete()
    return redirect('jobs:index')
