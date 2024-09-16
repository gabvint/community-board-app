from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Board
from .forms import BoardForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


class BoardCreate(CreateView):
    model = Board
    form_class = BoardForm
    # success_url = '/board/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BoardUpdate(UpdateView):
    model = Board
    fields = '__all__'
    
class BoardDelete(DeleteView):
    model = Board
    success_url = '/board/'
    
class Home(LoginView):
    template_name = 'home.html'
    
# Create your views here.
    

def about(request):
    return render(request, 'about.html')

def board_index(request): #displays all the items in the board
    board = Board.objects.all()
    return render(request, 'board/index.html', {'board': board})

def board_detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'board/detail.html', {'board': board}) 

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('board-index')
        
        else:
            error_message = 'Invalid sign up try again'
    form = UserCreationForm()
    context = {
        'form': form, 
        'error_message': error_message
    }   
    return render(request, 'signup.html', context)