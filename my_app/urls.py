from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'), 
    path('board/', views.board_index, name='board-index'),
    path('board/<int:board_id>/', views.board_detail, name='board-detail'), 
    path('board/create/', views.BoardCreate.as_view(), name='board-create'),
    path('board/<int:pk>/update/', views.BoardUpdate.as_view(), name='board-update'),
    path('board/<int:pk>/delete/', views.BoardDelete.as_view(), name='board-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

