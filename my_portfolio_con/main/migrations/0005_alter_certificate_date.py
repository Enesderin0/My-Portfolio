# Generated by Django 4.0.5 on 2022-06-06 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='date',
            field=models.CharField(max_length=30, verbose_name='date'),
        ),
    ]