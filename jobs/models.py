from datetime import datetime as dt

from django.db import models
from django.core.validators import ValidationError


class Position(models.Model):
    """Модель Должность"""
    name = models.CharField(
        verbose_name='Должность', db_index=True, unique=True,
        max_length=20, help_text='Введите название должности'
    )

    specialist = 'Специалист'
    clerical = 'Служащий'
    labourer = 'Рабочий'

    CATEGORY_CHOICES = [
        (specialist, 'Специалист'),
        (clerical, 'Служащий'),
        (labourer, 'Рабочий'),
    ]

    category = models.CharField(
        verbose_name='Категория', choices=CATEGORY_CHOICES,
        max_length=10, help_text='Выберите категорию'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Изменение строки поля Должность. Перевод первой буквы строки в
        верхний регистр, остальные в нижний
        """
        for field_name in ['name', ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Position, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Должности"
        verbose_name = "Должность"


class Employee(models.Model):
    """Модель Сотрудник"""
    first_name = models.CharField(
        verbose_name='Имя', max_length=30, help_text='Введите имя'
    )
    last_name = models.CharField(
        verbose_name='Фамилия', max_length=30, db_index=True,
        help_text='Введите фамилию',
    )
    patronymic = models.CharField(
        verbose_name='Отчество', max_length=30,
        blank=True, help_text='Введите отчество'
    )

    male = 'Мужской'
    female = 'Женский'

    SEX_CHOICES = [
        (male, 'Мужской'),
        (female, 'Женский'),
    ]

    sex = models.CharField(
        verbose_name='Пол', choices=SEX_CHOICES,
        max_length=7, help_text='Выберите пол'
    )
    dob = models.DateField(
        verbose_name='Дата рождения',
        help_text='Введите дату рождения',
    )
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, related_name='employees',
        blank=True, null=True, verbose_name='Должность',
        help_text='Выберите должность',
    )

    def __str__(self):
        return self.first_name + self.last_name

    def clean_fields(self, exclude=None):
        """
        Проверка значения поля Дата Рождения. Полное число лет
        не должно превышать 150 и не должно быть меньше 14.
        """
        date_now = dt.now().date()
        age = int((date_now - self.dob).days / 365.25)
        if age > 150:
            raise ValidationError({'dob': ["Сотруднику слишком много лет!", ]})
        elif age < 14:
            raise ValidationError({'dob': ["Сотруднику слишком мало лет!", ]})

    def save(self, *args, **kwargs):
        """
        Изменение строк полей ФИО. Перевод первой буквы строки в
        верхний регистр, остальные в нижний
        """
        for field_name in ['first_name', 'last_name', 'patronymic', ]:
            val = getattr(self, field_name, False)
            if val:
                setattr(self, field_name, val.capitalize())
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Сотрудники"
        verbose_name = "Сотрудник"
        unique_together = (("first_name", "last_name", "patronymic", "dob", ),)
        ordering = ['last_name', 'first_name', 'patronymic', ]
