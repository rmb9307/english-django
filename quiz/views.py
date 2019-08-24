from django.shortcuts import render
from .models import Quiz

def home(request):
    context = {
        'quizzes': Quiz.objects.all()
    }
    return render(request, 'quiz/home.html', context)

def about(request):
    return render(request, 'quiz/about.html', {'title': 'About'})