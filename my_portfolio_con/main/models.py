from email.mime import image
from email.policy import default
import numbers
from pyexpat import model
from tabnanny import verbose
from tkinter import N
from turtle import title
from unicodedata import name
from django.db import models
from ckeditor.fields import RichTextField

class Skills(models.Model):
    skill=models.CharField(verbose_name="skills",max_length=50,blank=False,null=False,)
    degree=models.IntegerField(verbose_name="degree",blank=False,null=False)
    color=models.CharField(verbose_name="color",max_length=50)
    
    def __str__(self):
        return self.skill


class About(models.Model):
    who=models.CharField(verbose_name="Who",max_length=100,null=False,blank=False)
    about= RichTextField()
        
    def __str__(self):
        return self.who

class Certificate(models.Model):
    certificate=models.CharField(verbose_name="title",max_length=200,null=False,blank=False)
    date=models.CharField(verbose_name="date",max_length=30,null=False,blank=False)
    url=models.URLField(verbose_name="URL",blank=True,null=True)

    def __str__(self):
        return self.certificate

class Education(models.Model):
    school=models.CharField(verbose_name="School" ,max_length=150,null=False,blank=False)
    date=models.CharField(verbose_name="Date",max_length=50,null=False,blank=False)
    branch=models.CharField(verbose_name="Branch",max_length=50,null=True,blank=True)

    def __str__(self):
        return self.school

class Works(models.Model):
    name=models.CharField(verbose_name="name",max_length=100,null=False,blank=False)
    image = models.ImageField(null=True, blank=True, verbose_name="Fotoğraf Ekle")
    def __str__(self):
        return self.name
    
         
    
    

