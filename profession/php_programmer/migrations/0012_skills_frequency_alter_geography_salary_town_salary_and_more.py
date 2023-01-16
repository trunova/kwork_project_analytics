# Generated by Django 4.1.5 on 2023-01-13 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('php_programmer', '0011_alter_geography_salary_town_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills_frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('frequency', models.IntegerField(verbose_name='Навыки')),
            ],
            options={
                'verbose_name': 'Навыки',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.AlterField(
            model_name='geography_salary_town',
            name='salary',
            field=models.FloatField(verbose_name='Зарплата'),
        ),
        migrations.CreateModel(
            name='Skills_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('skills_frequency', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='php_programmer.skills_frequency', verbose_name='Навыки')),
            ],
            options={
                'verbose_name': 'Навыки по годам',
                'verbose_name_plural': 'Навыки по годам',
            },
        ),
    ]