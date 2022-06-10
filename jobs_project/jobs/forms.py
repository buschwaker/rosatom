from django import forms

from .models import Position, Employee


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = '__all__'


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'
