from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Board:
    def __init__(self, title, description, date_posted):
        self.title = title
        self.description = description
        self.date_posted = date_posted

board = [
    Board("Community Meeting", "Monthly neighborhood meeting", "2024-09-10"),
    Board("Lost Dog", "Missing dog near 5th Avenue", "2024-09-08"),
    Board("Garage Sale", "Selling furniture and clothes", "2024-09-05"),
]

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def board_index(request):
    return render(request, 'board/index.html', {'board': board})