# Generated by Django 4.2.3 on 2023-07-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='course',
            field=models.ManyToManyField(to='course.course', verbose_name='Курс'),
        ),
    ]
