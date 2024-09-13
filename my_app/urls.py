from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path('board/', views.board_index, name='board_index'),
    path('board/<int:board_id>/', views.board_detail, name='board-detail'), 
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

