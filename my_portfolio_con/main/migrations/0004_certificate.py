# Generated by Django 4.0.5 on 2022-06-06 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.CharField(max_length=200, verbose_name='title')),
                ('date', models.TextField(max_length=30, verbose_name='date')),
            ],
        ),
    ]
