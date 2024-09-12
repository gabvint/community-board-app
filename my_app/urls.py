from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('board/', views.board_index, name='board_index'),
    
]
