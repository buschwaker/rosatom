from django.contrib import admin
from django.conf import settings

from .models import Position, Employee


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Класс, определяющий вид Position в административной панели"""
    list_display = (
        'name',
        'category',
    )
    search_fields = (
        'name',
    )
    list_filter = ('name',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Класс, определяющий вид Employee в административной панели"""
    list_display = (
        'last_name',
        'first_name',
        'patronymic',
        'position',
    )
    search_fields = (
        'last_name',
    )
    list_filter = ('last_name',)
    empty_value_display = settings.EMPTY_VALUE_DISPLAY
