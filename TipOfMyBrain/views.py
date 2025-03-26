
from django.shortcuts import render

from .models import Movie, UserAnswer


def home(request):
    return render(request, 'index.html')


def game_view(request):
   return render(request, 'game.html')