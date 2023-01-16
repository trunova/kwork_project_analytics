from django.contrib import admin
from php_programmer.models import *
from django.contrib.auth.models import Group, User

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'email']

@admin.register(Demand_year_salary)
class Demand_year_salaryAdmin(admin.ModelAdmin):
    list_display = ['year', 'salary']

@admin.register(Demand_year_vacancy)
class Demand_year_vacancyAdmin(admin.ModelAdmin):
    list_display = ['year', 'number_of_vacancies']

@admin.register(Demand_PHP_year_salary)
class Demand_PHP_year_salaryAdmin(admin.ModelAdmin):
    list_display = ['year', 'salary']

@admin.register(Demand_PHP_year_vacancy)
class Demand_PHP_year_vacancyAdmin(admin.ModelAdmin):
    list_display = ['year', 'number_of_vacancies']

@admin.register(Geography_salary_town)
class Geography_salary_townAdmin(admin.ModelAdmin):
    list_display = ['town', 'salary']

@admin.register(Geography_vacancy_town)
class Geography_vacancy_townAdmin(admin.ModelAdmin):
    list_display = ['town', 'share_of_vacancies']

@admin.register(Skills_frequency)
class Skills_frequencyAdmin(admin.ModelAdmin):
    list_display = ['skill', 'frequency']

@admin.register(Skills_year)
class Skills_yearAdmin(admin.ModelAdmin):
    list_display = ['year', 'skills_frequency']

@admin.register(Latest_vacancies)
class Latest_vacanciesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'key_skills', 'company', 'salary_from', 'salary_to', 'salary_currency', 'region', 'published_at']
