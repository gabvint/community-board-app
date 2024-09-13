from django.shortcuts import render
from django.http import HttpResponse
from .models import Board
# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def board_index(request): #displays all the items in the board
    board = Board.objects.all()
    return render(request, 'board/index.html', {'board': board})

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board/detail.html', {'board': board}) 