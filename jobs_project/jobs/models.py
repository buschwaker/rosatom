from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Position(models.Model):
    name = models.CharField(
        verbose_name='Должность', db_index=True, unique=True,
        max_length=50, help_text='Введите название должности'
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

    class Meta:
        verbose_name_plural = "Должности"
        verbose_name = "Должность"

    def __str__(self):
        return self.name


class Employee(models.Model):
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
    age = models.IntegerField(
        verbose_name='Возраст', help_text='Введите возраст',
        validators=[
          MaxValueValidator(150, 'Слишком большой возраст!'),
          MinValueValidator(14, 'Слишком маленький возраст'), ]
    )
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, related_name='employees',
        blank=True, null=True, verbose_name='Должность',
        help_text='Выберите должность',
    )

    class Meta:
        verbose_name_plural = "Сотрудники"
        verbose_name = "Сотрудник"
        ordering = ['last_name', 'first_name', 'patronymic', ]

    def __str__(self):
        return self.first_name + self.last_name
