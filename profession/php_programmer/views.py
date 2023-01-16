from django.shortcuts import render
from django.views import View
from php_programmer import *
from django.core.handlers.wsgi import WSGIRequest
from .forms import *
import csv
import re
import requests
import datetime
import json
import os
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

from django.http import HttpResponseRedirect
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth import authenticate, login


def dynamics_of_salary_levels():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'media/vacancies_dif_currencies.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dict_of_currencies = {'USD': 1, 'RUR': 0.015, 'EUR': 1.09, 'KZT': 0.0022, 'UAH': 0.027, 'BYR': 0.40,
                              'AZN': 0.59, 'UZS': 0.000088, 'KGS': 0.012, 'GEL': 0.37}
        dct = {}
        currency = []
        for row in reader:
            year = row["published_at"][:4]
            salary = []
            if len(row["salary_from"]) > 0:
                salary.append(float(row["salary_from"]) * dict_of_currencies[row["salary_currency"]])
            if len(row["salary_to"]) > 0:
                salary.append(float(row["salary_to"]) * dict_of_currencies[row["salary_currency"]])
            if len(salary) != 0:
                try:
                    dct[year] += [np.mean(salary)]
                except KeyError:
                    dct[year] = [np.mean(salary)]
        result = [(key, round(np.mean(dct[key]), 3)) for key in dct.keys()]
        return result

def dynamics_of_the_num_vacancies():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'media/vacancies_dif_currencies.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dct = {}
        for row in reader:
            year = row["published_at"][:4]
            vacancy = row["name"]
            try:
                dct[year] += [vacancy]
            except KeyError:
                dct[year] = [vacancy]
        result = [(key, len(dct[key])) for key in dct.keys()]
        return result


def dynamics_PHP_of_salary_levels():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'media/vacancies_dif_currencies.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dict_of_currencies = {'USD': 1, 'RUR': 0.015, 'EUR': 1.09, 'KZT': 0.0022, 'UAH': 0.027, 'BYR': 0.40,
                              'AZN': 0.59, 'UZS': 0.000088, 'KGS': 0.012, 'GEL': 0.37}
        i = 0
        dct = {}
        currency = []
        for row in reader:
            if row["name"] != "PHP-программист":
                continue
            # i+=1
            # if i == 80000: break
            year = row["published_at"][:4]
            salary = []

            if len(row["salary_from"]) > 0:
                salary.append(float(row["salary_from"]) * dict_of_currencies[row["salary_currency"]])
            if len(row["salary_to"]) > 0:
                salary.append(float(row["salary_to"]) * dict_of_currencies[row["salary_currency"]])
            if len(salary) != 0:
                try:
                    dct[year] += [np.mean(salary)]
                except KeyError:
                    dct[year] = [np.mean(salary)]
        result = [(key, round(np.mean(dct[key]), 3)) for key in dct.keys()]
        return result


def dynamics_PHP_of_the_num_vacancies():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'media/vacancies_dif_currencies.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dct = {}
        for row in reader:
            if row["name"] != "PHP-программист":
                continue
            year = row["published_at"][:4]
            vacancy = row["name"]
            try:
                dct[year] += [vacancy]
            except KeyError:
                dct[year] = [vacancy]
        result = [(key, len(dct[key])) for key in dct.keys()]
        return result


def wage_level_by_city():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'media/vacancies_dif_currencies.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dict_of_currencies = {'USD': 1, 'RUR': 0.015, 'EUR': 1.09, 'KZT': 0.0022, 'UAH': 0.027, 'BYR': 0.40,
                              'AZN': 0.59, 'UZS': 0.000088, 'KGS': 0.012, 'GEL': 0.37}
        dct = {}
        for row in reader:
            area = row["area_name"]
            salary = []
            if len(row["salary_from"]) > 0:
                salary.append(float(row["salary_from"]) * dict_of_currencies[row["salary_currency"]])
            if len(row["salary_to"]) > 0:
                salary.append(float(row["salary_to"]) * dict_of_currencies[row["salary_currency"]])
            if len(salary) != 0:
                try:
                    dct[area] += [np.mean(salary)]
                except KeyError:
                    dct[area] = [np.mean(salary)]

        result = [(key, np.mean(dct[key])) for key in dct.keys()]
        # result.sort(key=lambda x: x[1], reverse=True)
        return result

def vacancy_by_city():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'media/vacancies_dif_currencies.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dct = {}
        s = 0
        for row in reader:
            area = row["area_name"]
            s += 1
            try:
                dct[area] += 1
            except KeyError:
                dct[area] = 1
        result = [(key, dct[key] / s) for key in dct.keys()]
        return result


def skills_by_year():
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'media/vacancies_with_skills.csv')
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dct = {}
        for row in reader:
            skills = row["key_skills"]
            if skills:
                year = row["published_at"][:4]
                try:
                    for skill in skills.split("\n"):
                        try:
                            dct[year][skill] += 1
                        except KeyError:
                            dct[year][skill] = 1
                except KeyError:
                    skill_dict = {}
                    for skill in skills.split("\n"):
                        try:
                            skill_dict[skill] += 1
                        except KeyError:
                            skill_dict[skill] = 1
                    dct[year] = skill_dict
        for k in dct.keys():
            result = [(key, dct[k][key]) for key in dct[k].keys()]
            result.sort(key=lambda x: x[1], reverse=True)
            dct[k] = result[:10]
        return dct


class PhpProgrammerView(View):
    def get(self, request: WSGIRequest):
        context = {}
        # form1 = FileForm()
        # context['form1'] = form1
        return render(request, 'php_programmer/main_page.html', context)

    def post(self, request: WSGIRequest):
        context = {}
        # if request.POST.get('data'):
            # form1 = FileForm(request.POST, request.FILES)
            # form1.save()
            # return render(request, 'php_programmer/main_page.html', context)
            # return HttpResponseRedirect("/programmer/")
        return render(request, 'php_programmer/main_page.html', context)

class DemandView(View):
    def get(self, request: WSGIRequest):
        context = {}
        demands = [[Demand_year_salary.objects.all(), 'Динамика уровня зарплат по годам', 'Год', 'Уровень зарплат', 'demand_year_salary'],
                   [Demand_year_vacancy.objects.all(), 'Динамика количества вакансий по годам', 'Год', 'Количество вакансий', 'demand_year_vacancy'],
                   [Demand_PHP_year_salary.objects.all(), 'Динамика уровня зарплат по годам для выбранной профессии', 'Год', 'Уровень зарплат', 'demand_PHP_year_salary'],
                   [Demand_PHP_year_vacancy.objects.all(), 'Динамика количества вакансий по годам для выбранной профессии', 'Год', 'Количество вакансий', 'demand_PHP_year_vacancy'],
                   ]
        for demand in demands:
            fig, ax = plt.subplots()
            x = []
            y = []
            for d in demand[0]:
                x.append(d.year)
                try:
                    y.append(d.salary)
                except:
                    y.append(d.number_of_vacancies)
            plt.title(demand[1])
            plt.xlabel(demand[2])
            plt.ylabel(demand[3])
            ax.set_xticklabels(x, fontsize=8, color='black', rotation=90)
            plt.plot(x, y)
            fig.savefig('php_programmer/static/images/{img_name}.png'.format(img_name=demand[4]))
            demand[4] = f"images/{demand[4]}.png"
        context['demands'] = demands

        return render(request, 'php_programmer/demand.html', context)

    def post(self, request: WSGIRequest):
        context = {}
        if request.POST.get('data_analysis'):
            Demand_year_salary.objects.all().delete()
            Demand_year_vacancy.objects.all().delete()
            Demand_PHP_year_salary.objects.all().delete()
            Demand_PHP_year_vacancy.objects.all().delete()
            result1 = dynamics_of_salary_levels()
            result2 = dynamics_of_the_num_vacancies()
            result3 = dynamics_PHP_of_salary_levels()
            result4 = dynamics_PHP_of_the_num_vacancies()
            for year, salary in result1:
                m = Demand_year_salary(year=year, salary=salary)
                m.save()
            for year, number_of_vacancies in result2:
                m = Demand_year_vacancy(year=year, number_of_vacancies=number_of_vacancies)
                m.save()
            for year, salary in result3:
                m = Demand_PHP_year_salary(year=year, salary=salary)
                m.save()
            for year, number_of_vacancies in result4:
                m = Demand_PHP_year_vacancy(year=year, number_of_vacancies=number_of_vacancies)
                m.save()
            return HttpResponseRedirect("/programmer/demand/")

        return render(request, 'php_programmer/demand.html', context)


class GeographyView(View):
    def get(self, request: WSGIRequest):
        context = {}
        geography_salary_town = Geography_salary_town.objects.order_by('-salary')
        geography_vacancy_town = Geography_vacancy_town.objects.order_by('-share_of_vacancies')
        fig, ax = plt.subplots()
        x = []
        y = []
        i = 0
        for g in geography_salary_town:
            i += 1
            if g.salary < 4000: break
            x.append(g.town)
            y.append(g.salary)
        ax.set_xticklabels(x, fontsize=8, color='b', rotation=90)
        plt.title('Уровень зарплат по городам')
        plt.xlabel('Город')
        plt.ylabel('Зарплата')
        plt.plot(x, y)
        fig.savefig('php_programmer/static/images/geography_salary_town.png')

        fig, ax = plt.subplots()
        x = []
        y = []
        j = 0
        for g in geography_vacancy_town:
            j += 1
            if g.share_of_vacancies < 0.0007: break
            x.append(g.town)
            y.append(g.share_of_vacancies)
        ax.set_xticklabels(x, fontsize=8, color='b', rotation=90)
        plt.title('Доля вакансий по городам')
        plt.xlabel('Город')
        plt.ylabel('Доля')
        plt.plot(x, y)
        fig.savefig('php_programmer/static/images/geography_vacancy_town.png')
        context['geography_salary_town'] = geography_salary_town[:i]
        context['geography_vacancy_town'] = geography_vacancy_town[:j]
        return render(request, 'php_programmer/geography.html', context)

    def post(self, request: WSGIRequest):
        context = {}
        if request.POST.get('data_analysis'):
            Geography_salary_town.objects.all().delete()
            Geography_vacancy_town.objects.all().delete()
            result1 = wage_level_by_city()
            result2 = vacancy_by_city()
            for town, salary in result1:
                m1 = Geography_salary_town(town=town, salary=salary)
                m1.save()
            for town, share_of_vacancies in result2:
                m2 = Geography_vacancy_town(town=town, share_of_vacancies=share_of_vacancies)
                m2.save()
            return HttpResponseRedirect("/programmer/geography/")
        return render(request, 'php_programmer/geography.html', context)


class SkillsView(View): # skills_by_year
    def get(self, request: WSGIRequest):
        context = {}
        skills_year = Skills_year.objects.order_by('year')
        if not skills_year:
            return render(request, 'php_programmer/skills.html', context)
        year = skills_year[0].year
        lst = []
        data = []
        for skill_year in skills_year:
            if year == skill_year.year:
                lst.append((skill_year.skills_frequency.skill,skill_year.skills_frequency.frequency))
            else:
                lst.sort(key=lambda x: x[1], reverse=True)
                data.append((year, lst, f'images/skill_{year}.png'))
                lst = []
                year = skill_year.year
        lst.sort(key=lambda x: x[1], reverse=True)
        data.append((year, lst, f'images/skill_{year}.png'))
        for d in data:
            fig, ax = plt.subplots()
            ax.set_xticklabels([x[0] for x in d[1]], fontsize=8, color='b', rotation=90)
            plt.title(f'ТОП-10 навыков за {d[0]} год')
            plt.xlabel('Навык')
            plt.ylabel('Частота')
            plt.plot([x[0] for x in d[1]], [x[1] for x in d[1]])
            fig.savefig(f'php_programmer/static/{d[2]}')

        context['data'] = data
        return render(request, 'php_programmer/skills.html', context)

    def post(self, request: WSGIRequest):
        context = {}
        if request.POST.get('data_analysis'):
            Skills_frequency.objects.all().delete()
            Skills_year.objects.all().delete()
            results = skills_by_year()
            for key in results.keys():
                for result in results[key]:
                    m1 = Skills_frequency(skill=result[0], frequency=result[1])
                    m1.save()
                    m2 = Skills_year(year=key, skills_frequency=m1)
                    m2.save()
            return HttpResponseRedirect("/programmer/skills/")
        return render(request, 'php_programmer/skills.html', context)


class LatestVacanciesView(View):
    def get(self, request: WSGIRequest):
        context = {}
        Latest_vacancies.objects.all().delete()
        params = {
            'area': 113,
            'page': 0,
            'per_page': 100
        }
        response = requests.get('https://api.hh.ru/vacancies', params).json()
        data = response.get("items")
        sorted_data = sorted(data, key=lambda v: datetime.datetime.strptime(v['published_at'], '%Y-%m-%dT%H:%M:%S+%f'),
                             reverse=True)
        for row in sorted_data[:10]:
            vacancy = requests.get(str(row['url'])).json()
            vacancy_salary_from = vacancy['salary']['from'] if vacancy['salary'] else ''
            vacancy_salary_to = vacancy['salary']['to'] if vacancy['salary'] else ''
            vacancy_salary_currency = vacancy['salary']['currency'] if vacancy['salary'] else ''
            vacancy_salary_from = '' if vacancy_salary_from == None else vacancy_salary_from
            vacancy_salary_to = '' if vacancy_salary_to == None else vacancy_salary_to
            latest_vacancies = Latest_vacancies(
                title=vacancy['name'],
                description=re.sub(r'\<[^>]*\>', '', vacancy['description']),
                key_skills=', '.join([skill['name'] for skill in vacancy['key_skills']]),
                company=vacancy['employer']['name'],
                salary_from=vacancy_salary_from,
                salary_to=vacancy_salary_to,
                salary_currency=vacancy_salary_currency,
                region=vacancy['area']['name'],
                published_at=datetime.datetime.strptime(vacancy['published_at'], '%Y-%m-%dT%H:%M:%S+%f')
            )
            latest_vacancies.save()
        context['latest_vacancies'] = Latest_vacancies.objects.all()
        return render(request, 'php_programmer/latest_vacancies.html', context)

    def post(self, request: WSGIRequest):
        context = {}
        return render(request, 'php_programmer/latest_vacancies.html', context)