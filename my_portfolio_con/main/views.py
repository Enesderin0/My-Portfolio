from django.shortcuts import render
from main.models import Skills,About,Certificate,Education,Works

def home(request):
    skills= Skills.objects.all()
    abouts=About.objects.all()
    certificates=Certificate.objects.all()
    education=Education.objects.all()
    works=Works.objects.all()
    return render(request,'index.html',{
    'skills':skills,
    'abouts':abouts,
    'certificates':certificates,
    'education':education,
    'works':works,
    })


