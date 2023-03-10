# Generated by Django 4.1.5 on 2023-01-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('php_programmer', '0004_alter_profile_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files/', verbose_name='Файл')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
            ],
        ),
        migrations.AlterField(
            model_name='job_vacancy',
            name='published_at',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='latest_vacancies',
            name='published_at',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
