from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def board_index(request):
    board = Board.objects.all()
    return render(request, 'board/index.html', {'board': board})