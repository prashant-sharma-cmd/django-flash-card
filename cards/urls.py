from django.urls import path
from . import views

app_name = 'cards'
urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('<int:pk>/', views.DetailView.as_view(), name='card_detail'),
    path('create/', views.BoxCreateView.as_view(), name='box_create'),
    path('update/<int:pk>/', views.BoxUpdateView.as_view(), name='box_update'),
    path('delete/<int:pk>/', views.BoxDeleteView.as_view(), name='box_delete'),
]
