# Generated by Django 4.0.5 on 2022-06-06 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_certificate_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='URL'),
        ),
    ]
