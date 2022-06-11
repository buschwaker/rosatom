from datetime import datetime as dt
from datetime import date, timedelta
from django import forms

from .models import Position, Employee
from .widgets import DateSelectorWidget


class PositionForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = '__all__'


class EmployeeForm(forms.ModelForm):
    dob = forms.DateField(
        widget=DateSelectorWidget,
        label='Дата рождения',
        help_text='Введите дату рождения',
        initial=date.today() - timedelta(days=365.25*45),
    )

    class Meta:
        model = Employee
        fields = '__all__'
