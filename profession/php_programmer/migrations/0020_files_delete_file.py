# Generated by Django 4.1.5 on 2023-01-14 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('php_programmer', '0019_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file1', models.FileField(upload_to='', verbose_name='Файл vacancies_dif_currencies')),
                ('file2', models.FileField(upload_to='', verbose_name='Файл vacancies_with_skills')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]