# Generated by Django 4.2.3 on 2023-07-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lesson', verbose_name='Превью')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.URLField(max_length=30, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
