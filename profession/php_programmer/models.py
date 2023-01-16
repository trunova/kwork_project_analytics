from django.db import models
from django.contrib.auth.admin import User
import os

class Demand_year_salary(models.Model):
    year = models.CharField(verbose_name='Год', max_length=4, blank=False)
    salary = models.FloatField(verbose_name='Зарплата', blank=False)

    class Meta:
        verbose_name = 'Динамика уровня зарплат по годам'
        verbose_name_plural = 'Динамика уровня зарплат по годам'


class Demand_year_vacancy(models.Model):
    year = models.CharField(verbose_name='Год', max_length=4, blank=False)
    number_of_vacancies = models.IntegerField(verbose_name='Количество вакансий', blank=False)

    class Meta:
        verbose_name = 'Динамика количества вакансий по годам'
        verbose_name_plural = 'Динамика количества вакансий по годам'


class Demand_PHP_year_salary(models.Model):
    year = models.CharField(verbose_name='Год', max_length=4, blank=False)
    salary = models.FloatField(verbose_name='Зарплата', blank=False)

    class Meta:
        verbose_name = 'Динамика уровня зарплат по годам для выбранной профессии'
        verbose_name_plural = 'Динамика уровня зарплат по годам для выбранной профессии'


class Demand_PHP_year_vacancy(models.Model):
    year = models.CharField(verbose_name='Год', max_length=4, blank=False)
    number_of_vacancies = models.IntegerField(verbose_name='Количество вакансий', blank=False)

    class Meta:
        verbose_name = 'Динамика количества вакансий по годам для выбранной профессии'
        verbose_name_plural = 'Динамика количества вакансий по годам для выбранной профессии'


class Geography_salary_town(models.Model):
    town = models.CharField(verbose_name='Город', max_length=4, blank=False)
    salary = models.FloatField(verbose_name='Зарплата', blank=False)

    class Meta:
        verbose_name = 'Уровень зарплат по городам'
        verbose_name_plural = 'Уровень зарплат по городам'

class Geography_vacancy_town(models.Model):
    town = models.CharField(verbose_name='Город', max_length=4, blank=False)
    share_of_vacancies = models.FloatField(verbose_name='Доля вакансии', blank=False)

    class Meta:
        verbose_name = 'Доля вакансий по городам'
        verbose_name_plural = 'Доля вакансий по городам'

class Skills_frequency(models.Model):
    skill = models.CharField(verbose_name='Навык', max_length=100, blank=False)
    frequency = models.IntegerField(verbose_name='Частота', blank=False)

    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'


class Skills_year(models.Model):
    year = models.CharField(verbose_name='Год', max_length=4, blank=False)
    skills_frequency = models.ForeignKey(Skills_frequency, verbose_name='Навыки', default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Навыки по годам'
        verbose_name_plural = 'Навыки по годам'


class Latest_vacancies(models.Model):
    title = models.CharField(verbose_name='Название', max_length=1000, blank=False)
    description = models.TextField(verbose_name='Описание вакансии', blank=False)
    key_skills = models.TextField(verbose_name='Ключевые навыки', blank=False)
    company = models.CharField(verbose_name='Компания', max_length=200, blank=False)
    salary_from = models.CharField(verbose_name='Минимальная зарплата', max_length=100, blank=True, null=True)
    salary_to = models.CharField(verbose_name='Максимальная зарплата', max_length=100, blank=True, null=True)
    salary_currency = models.CharField(verbose_name='Валюта', max_length=20, blank=True, null=True)
    region = models.CharField(verbose_name='Название региона', max_length=200, blank=False)
    published_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=False, blank=False)

    def short_description(self):
        return f'{self.description[:100]} ...'

    class Meta:
        verbose_name = 'Последние вакансии'
        verbose_name_plural = 'Последние вакансии'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name='Почта', blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'

class Files(models.Model):
    file1 = models.FileField(verbose_name='Файл vacancies_dif_currencies')
    file2 = models.FileField(verbose_name='Файл vacancies_with_skills')
