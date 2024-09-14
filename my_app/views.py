from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Board
from .forms import BoardForm 


class BoardCreate(CreateView):
    model = Board
    form_class = BoardForm
    # success_url = '/board/'
    
class BoardUpdate(UpdateView):
    model = Board
    fields = '__all__'
    
class BoardDelete(DeleteView):
    model = Board
    success_url = '/board/'
    
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
